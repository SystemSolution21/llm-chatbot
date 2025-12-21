# app/train_rl.py

import torch
from app.config import LLM_MODEL
from app.db import SessionLocal
from app.models import Conversation
from transformers import AutoTokenizer, pipeline
from trl.models.modeling_value_head import AutoModelForCausalLMWithValueHead
from trl.trainer.ppo_config import PPOConfig
from trl.trainer.ppo_trainer import PPOTrainer


def main():
    # 1. Configuration
    config = PPOConfig(
        learning_rate=1.41e-5,
        mini_batch_size=4,
    )

    # 2. Load Policy Model
    # In a real scenario, load from "./sft_final_model"
    model = AutoModelForCausalLMWithValueHead.from_pretrained(LLM_MODEL)
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 3. Load Reward Model Pipeline
    try:
        reward_pipe = pipeline(
            "text-classification", model="./reward_final_model", tokenizer=tokenizer
        )
    except Exception:
        print("Reward model not found at ./reward_final_model. Skipping RL.")
        return

    # 4. Load Prompts (Environment)
    session = SessionLocal()
    convs = session.query(Conversation).limit(50).all()
    session.close()

    prompts = [c.user_message for c in convs if c.user_message is not None]
    if not prompts:
        print("No prompts found in DB.")
        return

    # 5. PPO Loop
    ppo_trainer = PPOTrainer(
        config=config,
        model=model,
        tokenizer=tokenizer,  # type: ignore
    )

    # Convert prompts to tensors
    input_tensors = [tokenizer(p, return_tensors="pt")["input_ids"][0] for p in prompts]

    print("Starting PPO Loop...")
    for i, input_tensor in enumerate(input_tensors):
        # Generate response
        # The `generate` method is on the model, not the PPOTrainer in older trl versions.
        # We call it on the model directly, adding a batch dimension with `unsqueeze(0)`.
        response_tensor = model.generate(input_tensor.unsqueeze(0), max_new_tokens=20)
        response_txt = tokenizer.decode(response_tensor[0])

        # Calculate Reward
        pipe_out = reward_pipe(response_txt, top_k=None)
        # Extract score for 'LABEL_1' (Positive)
        score = 0.0
        for item in pipe_out:
            if item["label"] == "LABEL_1":
                score = item["score"]
        reward = torch.tensor([score])

        # PPO Step
        ppo_trainer.step([input_tensor], [response_tensor[0]], [reward])  # type: ignore

    model.save_pretrained("./rl_final_model")
    tokenizer.save_pretrained("./rl_final_model")
    print("RL Training Complete.")


if __name__ == "__main__":
    main()
