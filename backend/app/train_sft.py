# app/train_sft.py

from app.config import LLM_MODEL
from app.db import SessionLocal
from app.models import Conversation, Feedback
from datasets import Dataset
from transformers import AutoTokenizer, TrainingArguments
from trl.trainer.sft_trainer import SFTTrainer


def main():
    # 1. Load data from DB
    session = SessionLocal()
    # Join to get only positively rated conversations (rating > 0)
    results = (
        session.query(Conversation)
        .join(Feedback, Conversation.id == Feedback.conversation_id)
        .filter(Feedback.rating > 0)
        .all()
    )
    session.close()

    if not results:
        print("No positive feedback data found for training.")
        return

    # 2. Format data for SFT
    data = [
        {"text": f"User: {r.user_message}\nAssistant: {r.model_response}"}
        for r in results
    ]
    dataset = Dataset.from_list(data)

    # Load Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 3. Configure Training
    training_args = TrainingArguments(
        output_dir="./sft_checkpoints",
        num_train_epochs=1,
        per_device_train_batch_size=2,
        save_steps=50,
        learning_rate=2e-5,
    )

    # 4. Train
    trainer = SFTTrainer(
        model=LLM_MODEL,
        train_dataset=dataset,
        dataset_text_field="text",  # type: ignore
        max_seq_length=512,  # type: ignore
        tokenizer=tokenizer,  # type: ignore
        args=training_args,
    )

    print("Starting SFT...")
    trainer.train()
    trainer.save_model("./sft_final_model")
    print("SFT Complete. Model saved to ./sft_final_model")


if __name__ == "__main__":
    main()
