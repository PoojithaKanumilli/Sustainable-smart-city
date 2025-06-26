import streamlit as st

def show():
    st.title("⚠️ Anomaly Checker")
    st.write("This module will detect anomalies in city metrics.")
    st.info("This is a mock response. Connect to IBM Granite LLM for real answers.")
    st.write("Upload your data file to check for anomalies.")
    uploaded_file = st.file_uploader("Upload data file", type=["csv", "xlsx"])
    if uploaded_file:
        st.write("Performing anomaly detection...")
        # Here you would implement the actual anomaly detection logic
        st.success("Anomaly detection completed. Check the results in the output section.")
    else:
        st.warning("Please upload a data file to proceed with anomaly detection.")