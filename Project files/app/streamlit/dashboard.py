import streamlit as st
import requests

st.set_page_config(page_title="Smart City Dashboard", layout="wide")

st.title("📊 Smart City Dashboard")
st.markdown("Welcome! This is your Streamlit dashboard for visualizing smart city data.")

# Get data from FastAPI
city = "Pune"  # You can change or make this dynamic with st.selectbox
try:
    response = requests.get(f"http://127.0.0.1:8000/dashboard/summary?city={city}")
    data = response.json()

    st.subheader("📍 Sensor Status")
    st.metric("Air Quality", data["air_quality"])
    st.metric("Traffic", data["traffic"])
    st.metric("Energy Usage", data["energy_usage"])
except:
    st.error("Failed to load data from API. Make sure FastAPI is running.")

st.markdown("📈 Future Plan section coming soon")
