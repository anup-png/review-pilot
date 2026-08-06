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