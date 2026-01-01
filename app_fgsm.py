from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import io
from PIL import Image
import base64
import random

app = FastAPI()

# Add CORS to allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FGSM Backend API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "fgsm-api"}

@app.post("/generate-adversarial/")
async def generate_adversarial(
    image: UploadFile = File(...),
    epsilon: float = Form(0.1)
):
    """Generate adversarial example using FGSM"""
    try:
        # Read the uploaded file
        contents = await image.read()
        
        # Process the image
        img = Image.open(io.BytesIO(contents))
        
        # Convert to grayscale and resize for MNIST (28x28)
        img = img.convert('L')
        img = img.resize((28, 28))
        
        # Convert to base64 for response
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()
        
        # Generate mock predictions
        original_pred = random.randint(0, 9)
        adversarial_pred = (original_pred + 1) % 10  # Different prediction
        
        # Create mock adversarial image (invert colors for demo)
        adversarial_img = Image.eval(img, lambda x: 255 - x)
        adversarial_buffered = io.BytesIO()
        adversarial_img.save(adversarial_buffered, format="PNG")
        adversarial_base64 = base64.b64encode(adversarial_buffered.getvalue()).decode()
        
        return {
            "success": True,
            "message": "Adversarial example generated successfully",
            "filename": image.filename,
            "epsilon": epsilon,
            "file_size": len(contents),
            "original_image": img_base64,
            "adversarial_image": adversarial_base64,
            "predictions": {
                "original": str(original_pred),
                "adversarial": str(adversarial_pred)
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "details": "Make sure you're uploading a valid image file"
        }

@app.post("/upload-test/")
async def upload_test(file: UploadFile = File(...)):
    """Simple test endpoint for image upload"""
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "message": "File upload successful"
    }

if __name__ == "__main__":
    print("Starting FGSM Backend on http://127.0.0.1:8000")
    print("API Docs: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)