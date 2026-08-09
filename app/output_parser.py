from pydantic import BaseModel, Field
from typing import Literal


class ReviewAnalyzer(BaseModel):

    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Sentiment of the customer review"
    )

    description: str = Field(
        description="One-line explanation of the sentiment"
    )


class NegativeReviewAnalyzer(BaseModel):

    emotion: str = Field(
        description="Customer emotion"
    )

    issue: str = Field(
        description="Main issue mentioned in the review"
    )

    urgency: Literal["low", "medium", "high"] = Field(
        description="Urgency level"
    )

    needs_human: bool = Field(
        description="Whether the review should be escalated to a human agent"
    )