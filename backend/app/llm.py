# app/llm.py

# Import local modules
from app.config import LLM_MODEL

# Import third-party libraries
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL, token=True)
# Ensure a pad token is set, which is required for many generation models
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

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
    do_sample=True,
    temperature=0.7,
)


def generate(prompt: str):
    """Generate text from a prompt."""

    return llm(prompt)[0]["generated_text"]
