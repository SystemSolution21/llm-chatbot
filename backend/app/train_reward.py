# app/train_reward.py

from app.config import LLM_MODEL
from app.db import SessionLocal
from app.models import Conversation, Feedback
from datasets import Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)


def main():
    # 1. Load data
    session = SessionLocal()
    results = (
        session.query(Conversation, Feedback)
        .join(Feedback, Conversation.id == Feedback.conversation_id)
        .all()
    )
    session.close()

    if not results:
        print("No feedback data found.")
        return

    # 2. Prepare data: Label 1 for positive rating, 0 for negative
    data_list = []
    for conv, fb in results:
        label = 1 if fb.rating > 0 else 0
        text = f"User: {conv.user_message}\nAssistant: {conv.model_response}"
        data_list.append({"text": text, "label": label})

    dataset = Dataset.from_list(data_list)

    # Tokenization
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    def tokenize_function(examples):
        return tokenizer(
            examples["text"], padding="max_length", truncation=True, max_length=512
        )

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    # 3. Model (Binary Classification)
    model = AutoModelForSequenceClassification.from_pretrained(LLM_MODEL, num_labels=2)
    model.config.pad_token_id = tokenizer.pad_token_id

    # 4. Train
    training_args = TrainingArguments(
        output_dir="./reward_checkpoints",
        num_train_epochs=3,
        per_device_train_batch_size=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets,
        tokenizer=tokenizer,  # type: ignore
    )

    print("Starting Reward Model Training...")
    trainer.train()
    trainer.save_model("./reward_final_model")
    print("Reward Model Training Complete.")


if __name__ == "__main__":
    main()
