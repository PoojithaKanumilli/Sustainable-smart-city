from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    
    reply = f"You said: {user_message}"

    # Make sure the response key is correct
    return JSONResponse(content={"response": reply})