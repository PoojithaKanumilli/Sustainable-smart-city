import streamlit as st

def show():
    st.title("📬 Citizen Feedback")
    name = st.text_input("Your Name")
    category = st.selectbox("Category", ["Water", "Air", "Energy", "Other"])
    message = st.text_area("Your Message")
    if st.button("Submit"):
        st.success("Thank you for your feedback!")
