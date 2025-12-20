# app/routes_chat.py

# Import local modules
from app.db import SessionLocal
from app.llm import generate
from app.models import Conversation
from app.rag import retrieve_context
from app.schemas import ChatRequest, ChatResponse

# Import third-party libraries
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Create a router instance
router = APIRouter()


def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)) -> ChatResponse:
    """Chat with the LLM."""

    context = retrieve_context(req.message)
    prompt = f"""
                Use the context to answer.

                Context:
                {context}

                Question:
                {req.message}
                """
    answer = generate(prompt)

    conversation = Conversation(user_message=req.message, model_response=answer)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return ChatResponse(conversation_id=str(conversation.id), answer=answer)
