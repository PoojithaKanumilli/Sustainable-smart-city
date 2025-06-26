import streamlit as st

def policy_ui():
    st.subheader("📄 Upload Policy Document")
    uploaded = st.file_uploader("Upload .txt or .csv file")
    if uploaded:
        text = uploaded.read().decode('utf-8')
        st.text_area("Raw Content", text, height=200)
        if st.button("Summarize"):
            st.success("Summary: This is a sample summary of the policy document.")
        