# app/routes_feedback.py

# Import local modules
from app.db import SessionLocal
from app.models import Feedback
from app.schemas import FeedbackRequest

# Import third-party libraries
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Create a router instance
router = APIRouter()


def get_db():
    """Get a database session."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/feedback")
def feedback(req: FeedbackRequest, db: Session = Depends(get_db)) -> dict[str, str]:
    """Add feedback to the database."""

    fb = Feedback(**req.dict())
    db.add(fb)
    db.commit()
    return {"status": "ok"}
