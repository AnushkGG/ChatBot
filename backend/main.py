from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv(dotenv_path="backend/.env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))




# CORS to allow frontend requests from anywhere (localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or use ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = genai.GenerativeModel("models/gemini-1.5-pro")

@app.get("/")
def read_root():
    return {"message": "Gemini Chatbot API running"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    try:
        response = model.generate_content(user_message)
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}