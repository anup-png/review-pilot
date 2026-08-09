import streamlit as st

from app.graph import review_graph

st.set_page_config(
    page_title="ReviewPilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 ReviewPilot")
st.subheader("AI Agent for Review Analysis & Smart Replies")

review = st.text_area(
    "Enter Customer Review",
    height=180
)

if st.button("Analyze Review"):

    if review.strip() == "":
        st.warning("Please enter a review.")
        st.stop()

    workflow = review_graph()

    result = workflow.invoke(
        {
            "review": review
        }
    )

    st.success("Analysis Complete")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Sentiment", result["sentiment"])

        st.write("### Description")
        st.info(result["description"])

        if result["sentiment"] == "negative":

            st.write("### Emotion")
            st.write(result["emotion"])

            st.write("### Issue")
            st.write(result["issue"])

            st.write("### Urgency")
            st.write(result["urgency"])

            st.write("### Needs Human")

            if result["needs_human"]:
                st.error("Yes")
            else:
                st.success("No")

    with col2:

        st.write("### AI Reply")

        st.text_area(
            "",
            result["reply"],
            height=250
        )