# app/db.py

# Import local modules
from app.settings import DATABASE_URL

# Import third-party libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create base model
Base = declarative_base()
