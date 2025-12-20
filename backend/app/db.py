# app/db.py

# Import third-party libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Import local modules
from backend.app.config import DATABASE_URL

# Create database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create base model
Base = declarative_base()
