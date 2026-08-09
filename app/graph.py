from langgraph.graph import StateGraph, START, END

from state import ReviewState

from nodes import (
    sentiment_classifier,
    route_review,
    positive_reply,
    neutral_reply,
    negative_review_analyzer,
    negative_reply_generator,
)


def review_graph():

    graph = StateGraph(ReviewState)

    graph.add_node("sentiment_classifier", sentiment_classifier)

    graph.add_node("positive_reply", positive_reply)
    graph.add_node("neutral_reply", neutral_reply)

    graph.add_node(
        "negative_review_analyzer",
        negative_review_analyzer,
    )

    graph.add_node(
        "negative_reply_generator",
        negative_reply_generator,
    )

    graph.add_edge(START, "sentiment_classifier")

    graph.add_conditional_edges(
        "sentiment_classifier",
        route_review,
        {
            "positive": "positive_reply",
            "neutral": "neutral_reply",
            "negative": "negative_review_analyzer",
        },
    )

    graph.add_edge(
        "negative_review_analyzer",
        "negative_reply_generator",
    )

    graph.add_edge("positive_reply", END)
    graph.add_edge("neutral_reply", END)
    graph.add_edge("negative_reply_generator", END)

    workflow = graph.compile()

    return workflow