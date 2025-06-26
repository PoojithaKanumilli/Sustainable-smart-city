# app/services/chat_assistant.py

from app.services.granite_llm import ask_granite

def ask_city_assistant(prompt: str) -> str:
    system_message = (
        "You are a helpful assistant who answers detailed questions "
        "about sustainability, green infrastructure, and pollution reduction."
    )
    full_prompt = f"<system>: {system_message}\n<user>: {prompt}\n"
    return ask_granite(full_prompt)