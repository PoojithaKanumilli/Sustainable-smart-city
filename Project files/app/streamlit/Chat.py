import streamlit as st
import requests

st.set_page_config(page_title="Chat Assistant", layout="wide")
st.title("💬 Smart City Chat Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask me anything about your smart city...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # --- Call your FastAPI/Granite/Mock AI model ---
    try:
        # Example: calling FastAPI endpoint (replace with real one)
        response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
        bot_reply = response.json().get("response", "Let me analyze and get back to you...")
    except:
        bot_reply = "⚠ Could not reach the assistant. Is your backend running?"

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})