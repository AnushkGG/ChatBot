# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Chatbot API is running."}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    # Simple rule-based logic
    if "hello" in user_message.lower():
        reply = "Hi there! How can I help you today?"
    else:
        reply = "I'm still learning. Please try saying 'hello'."

    return {"reply": reply}
