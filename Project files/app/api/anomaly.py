from fastapi import APIRouter, File, UploadFile, Form
from app.services.anomaly_file_checker import detect_anomaly_in_uploaded_csv

router = APIRouter()

@router.post("/detect-anomaly/")
async def detect_anomaly(
    file: UploadFile = File(...),
    kpi: str = Form(...),
    threshold: float = Form(...)
):
    content = (await file.read()).decode("utf-8")

    result = detect_anomaly_in_uploaded_csv(content, kpi, threshold)

    return result