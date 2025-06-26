from fastapi import APIRouter

router = APIRouter()

@router.get("/report-status")
def report_status(type: str):
    reports = {
        "air": "Air quality index is within safe limits.",
        "water": "Water purity is 92%.",
        "energy": "Energy consumption is reduced by 15%.",
        "waste": "Recycling rate has increased by 10%."
    }
    return {"report": reports.get(type.lower(), "No report available for this type.")}