# app/llm.py

# Import local modules
from app.config import LLM_MODEL

# Import third-party libraries
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
model = AutoModelForCausalLM.from_pretrained(LLM_MODEL, device_map="auto")

# Create a pipeline for text generation
llm = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
)


def generate(prompt: str):
    """Generate text from a prompt."""

    return llm(prompt)[0]["generated_text"]
