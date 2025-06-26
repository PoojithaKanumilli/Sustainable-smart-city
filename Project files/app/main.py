from fastapi import FastAPI, Form

from app.api.chat_router import router as chat_router
from app.api.policy_router import router as policy_router
from app.api.eco_tips_router import router as eco_tips_router
from app.api.feedback_router import router as feedback_router
from app.api.report_router import router as report_router
from app.api.vector_router import router as vector_router
from app.api.kpi_upload_router import router as kpi_upload_router
from app.api.dashboard_router import router as dashboard_router
from app.services import report_generator
from fastapi.responses import FileResponse
from app.api import anomaly
from app.api import upload, search

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Registering all routers
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(policy_router, prefix="/policy", tags=["Policy"])
app.include_router(eco_tips_router, prefix="/eco-tips", tags=["Eco Tips"])
app.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])
app.include_router(report_router, prefix="/report", tags=["Report"])
app.include_router(vector_router, prefix="/vector", tags=["Vector"])
app.include_router(kpi_upload_router, prefix="/kpi-upload", tags=["KPI Upload"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(anomaly.router)
app.include_router(upload.router)
app.include_router(search.router)
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/sustainability", response_class=HTMLResponse)
def sustainability(request: Request):
    return templates.TemplateResponse("sustainability.html", {"request": request})

@app.get("/report")
def generate_report():
    return {"message": "Report has been generated!"}

    if format == "markdown":
        path = report_generator.generate_markdown_report(summary)
        return FileResponse(path, media_type="text/markdown", filename=path.name)

    elif format == "pdf":
        path = report_generator.generate_pdf_report(summary)
        return FileResponse(path, media_type="application/pdf", filename=path.name)

    else:
        return {"summary": summary}