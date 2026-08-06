from graph import review_graph

initial_state={
    "review":"product rating is 1 star and i dont like it "
}

workflow = review_graph()
result = workflow.invoke(initial_state)
print(result)
