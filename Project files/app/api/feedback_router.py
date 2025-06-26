from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Feedback(BaseModel):
    name: str
    feedback: str

@router.post("/submit-feedback")
def submit_feedback(feedback_data: Feedback):
    # You can later save this to a database or file
    return {"message": "Feedback submitted successfully", "data": feedback_data}