from langgraph.graph import StateGraph,START,END
from nodes import review_analyzer,positive_reply,negative_analysis,neutral_reply,route_review
from state import ReviewState

def review_graph():
    graph = StateGraph(ReviewState)

    graph.add_node('review_analyzer',review_analyzer)

    graph.add_node("positive_reply", positive_reply)
    graph.add_node("neutral_reply", neutral_reply)
    graph.add_node("negative_analysis", negative_analysis)

    graph.add_edge(START,'review_analyzer')
    graph.add_conditional_edges(
    "review_analyzer",
    route_review,
    {
        "positive": "positive_reply",
        "negative": "negative_analysis",
        "neutral": "neutral_reply",
    },

)
    graph.add_edge("positive_reply", END)
    graph.add_edge("neutral_reply", END)
    graph.add_edge("negative_analysis", END)

    workflow = graph.compile()
    return workflow

