# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from SRC.gongju_response import generate_response

app = FastAPI()

# Allow CORS for frontend (Wix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later, replace with your Wix domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Updated request model
class MessageRequest(BaseModel):
    input: str
    user_id: str = "default"
    password: str | None = None  # <- This is the missing piece

@app.post("/chat")
async def chat(request: MessageRequest):
    print(f"🧪 Received user_id: {request.user_id}")
    print(f"🧪 Received password: {request.password}")

    # ✅ Pass all values to Gongju
    reply = generate_response(
        request.input,
        user_id=request.user_id,
        password=request.password
    )
    return {"response": reply}
