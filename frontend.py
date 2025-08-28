import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Microservices Client", layout="wide")

st.title("🤖  AI Microservices with LangChain")
st.caption("A simple Streamlit frontend to interact with the FastAPI AI services.")

tab1, tab2, tab3 = st.tabs(["📝 Summarize", "❓ Q&A (RAG)", "🗺️ Learning Path"])

with tab1:
    st.header("Text Summarization")
    summarize_text = st.text_area(
        "Enter the text you want to summarize:", height=200, key="summarize_text"
    )
    if st.button("Summarize", key="summarize_button"):
        if summarize_text:
            with st.spinner("Summarizing..."):
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/summarize", json={"text": summarize_text}
                    )
                    response.raise_for_status()  
                    result = response.json()
                    st.success("Summary:")
                    st.write(result.get("summary"))
                except requests.exceptions.RequestException as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text to summarize.")

with tab2:
    st.header("Question Answering over Documents")
    st.info("This Q&A system answers questions based on a pre-loaded document about Python.")
    qa_question = st.text_input("Enter your question:", key="qa_question")
    if st.button("Ask", key="qa_button"):
        if qa_question:
            with st.spinner("Searching for an answer..."):
                try:
                    response = requests.post(f"{BACKEND_URL}/qa", json={"question": qa_question})
                    response.raise_for_status()
                    result = response.json()
                    st.success("Answer:")
                    st.write(result.get("answer"))
                except requests.exceptions.RequestException as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a question.")

with tab3:
    st.header("Personalized Learning Path Generator")
    profile = st.text_area(
        "Your Profile:", help="Describe your current skills and experience.", key="profile"
    )
    goal = st.text_input("Your Goal:", help="What do you want to learn or achieve?", key="goal")
    if st.button("Generate Path", key="learn_path_button"):
        if profile and goal:
            with st.spinner("Generating your learning path..."):
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/learn-path", json={"profile": profile, "goal": goal}
                    )
                    response.raise_for_status()
                    result = response.json()
                    st.success("Your Custom Learning Path:")
                    st.markdown(result.get("learning_path"))
                except requests.exceptions.RequestException as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill in both your profile and goal.")