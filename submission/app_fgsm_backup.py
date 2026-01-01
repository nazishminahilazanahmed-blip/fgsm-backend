from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import torch
import numpy as np
from PIL import Image
import io
import base64

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FGSM Backend API is running"}

@app.post("/generate-adversarial/")
async def generate_adversarial(
    image: UploadFile = File(...),
    epsilon: float = Form(0.1)
):
    """
    Generate adversarial example using FGSM
    """
    try:
        # Read image
        contents = await image.read()
        pil_image = Image.open(io.BytesIO(contents)).convert('L')  # Convert to grayscale
        
        # Convert to numpy array
        img_array = np.array(pil_image)
        
        # For demo purposes, return mock data
        # In real implementation, you would:
        # 1. Load your model
        # 2. Generate adversarial example
        # 3. Return results
        
        # Mock prediction
        import random
        original_pred = random.randint(0, 9)
        adversarial_pred = (original_pred + 1) % 10
        
        # Convert image to base64 for response
        buffered = io.BytesIO()
        pil_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return {
            "message": "Adversarial example generated",
            "epsilon": epsilon,
            "original_image": img_str,  # Base64 encoded
            "adversarial_image": img_str,  # Same for demo (replace with actual adversarial)
            "predictions": {
                "original": str(original_pred),
                "adversarial": str(adversarial_pred)
            }
        }
        
    except Exception as e:
        return {"error": str(e)}

# Add other endpoints you might have...