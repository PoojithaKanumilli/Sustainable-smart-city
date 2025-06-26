from fastapi import APIRouter

router = APIRouter()

@router.get("/get-eco-tips")
def get_eco_tips(topic: str):
    tips = {
        "energy": "Turn off lights when not in use.",
        "water": "Fix leaky faucets.",
        "waste": "Reuse and recycle materials."
    }

    return {"tip": tips.get(topic.lower(), "No tip available for this topic.")}