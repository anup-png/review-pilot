def review_analyzer_prompt(review: str) -> str:
    return f"""
You are an expert sentiment classifier.

Analyze the following customer review.

Tasks:
1. Classify the sentiment as one of:
   - positive
   - negative
   - neutral

2. Provide a one-line explanation for your classification.

Review:
{review}
"""