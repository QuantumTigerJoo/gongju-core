from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from SRC.gongju_response import generate_response

app = FastAPI()

# Allow CORS for frontend (Wix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔒 Replace with https://www.gongju-ai.com later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request schema (no password)
class MessageRequest(BaseModel):
    input: str
    user_id: str = "default"

@app.post("/chat")
async def chat(request: MessageRequest):
    print(f"🧪 Received user_id: {request.user_id}")

    reply = generate_response(
        request.input,
        user_id=request.user_id
    )
    return {"response": reply}
