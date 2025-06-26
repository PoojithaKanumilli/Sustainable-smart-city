import streamlit as st

def chat_ui():
    st.subheader("🤖 Ask the City Assistant")
    prompt = st.text_area("Ask your question:")
    if st.button("Submit"):
        response = f"Mock response to: {prompt}"
        st.success(response)
    st.info("This is a mock response. Connect to IBM Granite LLM for real answers.")