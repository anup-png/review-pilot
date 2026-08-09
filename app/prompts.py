def review_analyzer_prompt(review: str):

    return f"""
You are an expert sentiment classifier.

Analyze the customer review.

Tasks:
1. Classify the sentiment as:
   - positive
   - negative
   - neutral

2. Give a one-line explanation.

Review:
{review}
"""


def positive_reply_prompt(review: str):

    return f"""
You are a customer support assistant.

Write a warm and professional thank-you reply.

Review:
{review}
"""


def neutral_reply_prompt(review: str):

    return f"""
You are a customer support assistant.

Generate a polite reply.

Thank the customer and ask if they have any suggestions for improvement.

Review:
{review}
"""


def negative_review_analyzer_prompt(review: str):

    return f"""
You are an expert customer support analyst.

Analyze the negative review.

Return:

1. Customer emotion
2. Main issue
3. Urgency (low, medium or high)
4. Whether this requires a human agent

Review:
{review}
"""


def negative_reply_prompt(
    review: str,
    emotion: str,
    issue: str,
    urgency: str,
):

    return f"""
You are a professional customer support executive.

Customer review:
{review}

Detected emotion:
{emotion}

Issue:
{issue}

Urgency:
{urgency}

Generate an empathetic and professional reply.

Do not promise anything unrealistic.

Keep the reply under 80 words.
"""