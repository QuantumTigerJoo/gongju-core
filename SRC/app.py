# app.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gongju_response import generate_response

app = FastAPI()

# Allow CORS for frontend (e.g. Wix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your Wix domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    input: str
    user_id: str

@app.post("/chat")
async def chat(request: MessageRequest):
    reply = generate_response(request.input)
    return {"response": reply}
