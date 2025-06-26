import streamlit as st

st.set_page_config(page_title="Smart City Assistant", layout="wide")

st.title("🏙 Welcome to the Smart City Assistant")

st.sidebar.title("smart city assistant")

st.markdown("### 📚 Explore All Features Using the Sidebar")

pages = {
    "📊 Dashboard Summary": "Monitor water and energy usage.",
    "💬 Citizen Feedback": "Submit and review public feedback.",
    "🌱 Eco Tips": "Get environment-friendly lifestyle suggestions.",
    "📈 KPI Forecasting": "See predictive analytics of smart city KPIs.",
    "🚨 Anomaly Detection": "Identify unusual sensor activity or city data spikes.",
    "📃 Sustainability Report": "Generate automated sustainability reports.",
    "📜 Policy Summarizer": "Summarize uploaded policies using AI.",
    "🤖 Chat Assistant": "Ask your AI assistant questions about city insights."
}

for name, desc in pages.items():
    st.markdown(f"{name}** — {desc}")

st.info("➡ Use the *sidebar* on the left to navigate to any page.")