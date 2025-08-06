from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, set specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message")

    if not message:
        return {"error": "Message is required"}

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": message},
            timeout=30,
            stream=True
        )

        if response.status_code == 200:
            full_response = ""
            for line in response.iter_lines():
                if line:
                    try:
                        obj = __import__('json').loads(line.decode('utf-8'))
                        full_response += obj.get("response", "")
                    except Exception:
                        continue
            return {"response": full_response or "No response"}
        else:
            return {"error": "Ollama returned non-200 status"}
    except Exception as e:
        return {"error": str(e)}
