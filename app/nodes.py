from state import ReviewState

from llm import get_model

from output_parser import (
    ReviewAnalyzer,
    NegativeReviewAnalyzer,
)

from prompts import (
    review_analyzer_prompt,
    negative_review_analyzer_prompt,
    positive_reply_prompt,
    neutral_reply_prompt,
    negative_reply_prompt,
)


# -----------------------------
# Sentiment Classifier
# -----------------------------
def sentiment_classifier(state: ReviewState):

    review = state["review"]

    model = get_model()

    prompt = review_analyzer_prompt(review)

    structured_model = model.with_structured_output(ReviewAnalyzer)

    result = structured_model.invoke(prompt)

    return {
        "sentiment": result.sentiment,
        "description": result.description,
    }


# -----------------------------
# Positive Reply
# -----------------------------
def positive_reply(state: ReviewState):

    model = get_model()

    prompt = positive_reply_prompt(state["review"])

    result = model.invoke(prompt)

    return {
        "reply": result.content
    }


# -----------------------------
# Neutral Reply
# -----------------------------
def neutral_reply(state: ReviewState):

    model = get_model()

    prompt = neutral_reply_prompt(state["review"])

    result = model.invoke(prompt)

    return {
        "reply": result.content
    }


# -----------------------------
# Negative Review Analyzer
# -----------------------------
def negative_review_analyzer(state: ReviewState):

    review = state["review"]

    model = get_model()

    prompt = negative_review_analyzer_prompt(review)

    structured_model = model.with_structured_output(
        NegativeReviewAnalyzer
    )

    result = structured_model.invoke(prompt)

    return {
        "emotion": result.emotion,
        "issue": result.issue,
        "urgency": result.urgency,
        "needs_human": result.needs_human,
    }


# -----------------------------
# Negative Reply Generator
# -----------------------------
def negative_reply_generator(state: ReviewState):

    model = get_model()

    prompt = negative_reply_prompt(
        review=state["review"],
        emotion=state["emotion"],
        issue=state["issue"],
        urgency=state["urgency"],
    )

    result = model.invoke(prompt)

    return {
        "reply": result.content
    }


# -----------------------------
# Router
# -----------------------------
def route_review(state: ReviewState):

    if state["sentiment"] == "positive":
        return "positive"

    if state["sentiment"] == "negative":
        return "negative"

    return "neutral"