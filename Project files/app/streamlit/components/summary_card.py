import streamlit as st

def kpi_card(title, value, unit="", color="green"):
    st.markdown(
        f"""
        <div style="padding: 20px; border-radius: 15px; background-color: #f0f2f6; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); margin-bottom: 10px;">
            <h4 style="color: {color}; margin-bottom: 0;">{title}</h4>
            <h2 style="margin-top: 5px;">{value} {unit}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
