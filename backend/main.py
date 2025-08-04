# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np

app = FastAPI()

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
with open("backend/crop_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "Crop Recommendation API running"}

@app.post("/recommend")
async def recommend_crop(request: Request):
    data = await request.json()
    features = [
        data["N"], data["P"], data["K"],
        data["temperature"], data["humidity"],
        data["ph"], data["rainfall"]
    ]
    prediction = model.predict([features])[0]
    return {"recommended_crop": prediction}
