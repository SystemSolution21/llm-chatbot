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

    message: str - The user's message.
    """

    message: str


class ChatResponse(BaseModel):
    """
    Schema for the chat response.

    conversation_id: str - The ID of the conversation.

    answer: str - The model's response.
    """

    conversation_id: str
    answer: str


class FeedbackRequest(BaseModel):
    """
    Schema for the feedback request.

    conversation_id: str - The ID of the conversation.

    rating: int - The rating of the response.

    corrected_answer: Optional[str] - The corrected answer (if any).

    issue: Optional[str] - The issue with the response (if any).
    """

    conversation_id: str
    rating: int
    corrected_answer: Optional[str] = None
    issue: Optional[str] = None
