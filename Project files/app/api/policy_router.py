from fastapi import APIRouter

router = APIRouter()

@router.get("/get-policy")
def get_policy(type: str):
    policies = {
        "energy": "Use renewable energy sources.",
        "water": "Implement water-saving measures.",
        "waste": "Follow proper waste segregation.",
        "transport": "Promote use of public transportation."
    }
    return {"policy": policies.get(type.lower(), "No policy found for this type.")}