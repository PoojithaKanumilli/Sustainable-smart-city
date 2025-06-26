from fpdf import FPDF
import streamlit as st

def generate_report(data_dict, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, value in data_dict.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(filename)
    st.success(f"PDF Report '{filename}' generated!")
    with open(filename, "rb") as file:
        st.download_button("📥 Download Report", data=file, file_name=filename)
