import streamlit as st

def show():
    st.title("🌱 Eco Tips")
    tip_keyword = st.text_input("Enter topic (e.g. water, energy)")
    if tip_keyword:
        st.info(f"Tip for {tip_keyword}: Use LED lights to save energy!")
    else:
        st.info("Enter a topic to get eco-friendly tips.")