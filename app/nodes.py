from state import ReviewState
from llm import get_model
from output_parser import ReviewAnalzer
from prompts import review_analyzer_prompt

def review_analyzer(state:ReviewState):

    review = state['review']

    model =get_model()
    prompt = review_analyzer_prompt(review=review)
    structured_model = model.with_structured_output(ReviewAnalzer)

    result = structured_model.invoke(prompt)
    print(result)

    return {
    "sentiment": result.sentiment,
    "description": result.description
    }


def positive_reply(state):
    print("Positive Path")
    return {"reply": "Thank you for your feedback!"}


def neutral_reply(state):
    print("Neutral Path")
    return {"reply": "Thank you for your review."}


def negative_analysis(state):
    print("Negative Path")
    return {"reply": "We're sorry about your experience.Kindly explain more about the issue."}

def route_review(state: ReviewState):

    sentiment = state["sentiment"]

    if sentiment == "positive":
        return "positive"

    elif sentiment == "negative":
        return "negative"

    return "neutral"