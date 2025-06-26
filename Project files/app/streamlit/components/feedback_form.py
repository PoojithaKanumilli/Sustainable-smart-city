import streamlit as st

def feedback_ui():
    st.subheader("📬 Submit Feedback")
    name = st.text_input("Your Name")
    category = st.selectbox("Category", ["Water", "Air", "Energy", "Transport", "Other"])
    message = st.text_area("Your Feedback")

    if st.button("Send"):
        st.success("Thanks for your feedback!")
        return {"name": name, "category": category, "message": message}
    return None
