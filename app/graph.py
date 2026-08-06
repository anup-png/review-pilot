from langgraph.graph import StateGraph,START,END
from nodes import review_analyzer
from state import ReviewState

def review_graph():
    graph = StateGraph(ReviewState)

    graph.add_node('review_analyzer',review_analyzer)

    graph.add_edge(START,'review_analyzer')
    graph.add_edge('review_analyzer',END)

    workflow = graph.compile()
    return workflow

