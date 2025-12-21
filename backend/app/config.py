# app/config.py

# Import built-in libraries
import os

# Import third-party libraries
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "")
LLM_MODEL = os.getenv("LLM_MODEL", "")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")
if not VECTOR_DB_PATH:
    raise ValueError("CHROMA_PATH is not set")
if not LLM_MODEL:
    raise ValueError("LLM_MODEL is not set")
if not EMBEDDING_MODEL:
    raise ValueError("EMBEDDING_MODEL is not set")
