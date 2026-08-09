from typing import Literal
from typing_extensions import TypedDict


class ReviewState(TypedDict):
    review: str

    sentiment: Literal["positive", "negative", "neutral"]
    description: str

    emotion: str
    issue: str
    urgency: str
    needs_human: bool

    reply: str