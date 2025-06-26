from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard(category: str):
    summaries = {
        "energy": "Energy usage reduced by 12% this month.",
        "water": "Water consumption decreased by 8%.",
        "waste": "Waste recycling increased by 20%.",
        "transport": "Public transport usage grew by 15%."
    }
    return {"summary": summaries.get(category.lower(), "No summary available for this category.")}