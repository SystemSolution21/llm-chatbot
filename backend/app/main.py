# app/main.py

# Import local modules
from app.db import Base, engine
from app.routes_chat import router as chat_router
from app.routes_feedback import router as feedback_router

# Import third-party libraries
from fastapi import FastAPI

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(chat_router)
app.include_router(feedback_router)
