@echo off
echo Starting FGSM Backend API...
echo ============================
cd /d D:\FGSM

REM Activate virtual environment
if exist "venv\Scripts\activate" (
    call venv\Scripts\activate
    echo Virtual environment activated
) else (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
)

REM Run the FastAPI server
echo Starting server on http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
python -m uvicorn app_fgsm:app --reload --host 127.0.0.1 --port 8000

pause