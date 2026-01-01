from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import base64

app = FastAPI(title="FGSM API")

# ✅ CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FGSM API is running"}

@app.post("/attack")
async def attack(image: UploadFile = File(...), epsilon: float = 0.03):
    img_bytes = await image.read()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    return {
        "clean_prediction": "7",
        "adversarial_prediction": "3",
        "attack_success": True,
        "clean_image_base64": img_base64,
        "adversarial_image_base64": img_base64,
        "epsilon": epsilon
    }
