# app/settings.py

# Import built-in libraries
import os
import sys

# Import third-party libraries
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
DATABASE_URL: str = str(os.getenv("DATABASE_URL"))
VECTOR_DB_PATH: str = str(os.getenv("VECTOR_DB_PATH"))
LLM_MODEL: str = str(os.getenv("LLM_MODEL"))

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")
    sys.exit(1)
if not VECTOR_DB_PATH:
    raise ValueError("CHROMA_PATH is not set")
    sys.exit(1)
if not LLM_MODEL:
    raise ValueError("LLM_MODEL is not set")
    sys.exit(1)
