import streamlit as st

def show():
    st.title("📄 Policy Document Search")
    uploaded_file = st.file_uploader("Upload policy document")
    if uploaded_file:
        st.write("Performing summarization / search...")
        
