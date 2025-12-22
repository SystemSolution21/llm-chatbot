# app/llm.py

# Import local modules
from app.config import LLM_MODEL

# Import third-party libraries
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL, token=True)
model = AutoModelForCausalLM.from_pretrained(
    LLM_MODEL, device_map="auto", dtype="auto", token=True
)

# Create a pipeline for text generation
llm = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    return_full_text=False,
)


def generate(prompt: str):
    """Generate text from a prompt."""

    return llm(prompt)[0]["generated_text"]
