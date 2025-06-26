from app.services.granite_llm import ask_granite

def summarize_policy(text: str) -> str:
    prompt = (
        "You are a smart city assistant AI. Read the following policy text carefully "
        "and generate a concise summary of *at least 50 words* using simple and clear language.\n\n"
        f"Policy Text:\n{text}\n\n"
        "Summary:"
    )
    return ask_granite(prompt)
