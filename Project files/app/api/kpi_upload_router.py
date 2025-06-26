from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse
from app.services.kpi_file_forecaster import forecast_from_uploaded_csv

router = APIRouter()

# Existing endpoint for uploading document
@router.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...)):
    return {"message": "File uploaded successfully"}

# ✅ New endpoint for forecasting KPI from uploaded CSV
@router.post("/forecast_kpi")
async def forecast_kpi(file: UploadFile = File(...), kpi: str = Form(...)):
    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        result = forecast_from_uploaded_csv(decoded, kpi)

        if "error" in result:
            return JSONResponse(status_code=400, content=result)
        return result

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})