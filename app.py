
import streamlit as st
from llm import ask_video

st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎬"
)

st.title("🎬 AI Video Assistant")
st.write("Apne video ke baare mein koi bhi sawal poocho.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Video ke baare mein poocho...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Video se jawab dhoondh raha hoon..."):
            answer = ask_video(question)
            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
