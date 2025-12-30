from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import torch

app = FastAPI(
    title="FGSM Adversarial Attack API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FGSM API is running"}

@app.post("/attack")
def attack(image: UploadFile = File(...), epsilon: float = 0.03):
    return {
        "filename": image.filename,
        "epsilon": epsilon,
        "status": "Attack endpoint working"
    }
