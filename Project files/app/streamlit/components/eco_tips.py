import streamlit as st

def eco_tip_ui():
    st.subheader("🌱 Get Eco-Friendly Tips")
    topic = st.text_input("Enter topic (e.g. electricity, water)")
    if st.button("Get Tip"):
        st.info(f"Tip for {topic}: Use public transport to reduce emissions.")
    st.info("Enter a topic to get eco-friendly tips.")
    return topic if topic else None