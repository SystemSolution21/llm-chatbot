# app/schemas.py
"""
This module contains the schemas for the API.
"""

# Import built-in libraries
from typing import Optional

# Import third-party libraries
from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Schema for the chat request.
    """

    message: str


class ChatResponse(BaseModel):
    """
    Schema for the chat response.
    """

    conversation_id: str
    answer: str


class FeedbackRequest(BaseModel):
    """
    Schema for the feedback request.
    """

    conversation_id: str
    rating: int
    corrected_answer: Optional[str] = None
    issue: Optional[str] = None
