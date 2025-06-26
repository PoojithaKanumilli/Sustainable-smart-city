import os
import json
from dotenv import load_dotenv
from typing import Dict

# Load environment variables
load_dotenv()
API_KEY = os.getenv("1qfUmdvTPtl6LbYA3vCyDqYBUhuTZY_9rfwE7CC6R84s")
MODEL = "ibm-granite/granite-3.3-2b-instruct" 

# Function to build prompt
def build_prompt(kpis: Dict[str, float]) -> str:
    prompt = "Generate a smart city status report based on the following KPIs:\n\n"
    for kpi, value in kpis.items():
        prompt += f"- {kpi}: {value}\n"
    prompt += "\nThe report should be formal, insightful, and concise.\n"
    return prompt

# Function to generate report
def generate_report(kpis: Dict[str, float]) -> str:
    prompt = build_prompt(kpis)

    # If using IBM watsonx or OpenAI's API
    # Replace this mock return with actual API call
    response = {
        "text": "Report Placeholder: This is where the AI-written report would appear."
    }

    # --- Replace above with your actual API logic ---
    import openai
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    max_tokens=500,
    temperature=0.7,
    )
    return response['choices'][0]['message']['content']

    return response["text"]

# Example usage
if __name__ == "_main_":
    kpis = {
        "Electricity Usage": 1200,
        "Water Consumption": 850,
        "Air Quality Index": 42,
        "Traffic Congestion Level": 68
    }

    report = generate_report(kpis)
    print("\n📄 AI-Generated Report:\n")
    print(report)

    