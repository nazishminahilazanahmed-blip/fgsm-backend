@echo off
echo Building and deploying FGSM Backend to AWS...
echo ===========================================
cd /d D:\FGSM

REM Activate virtual environment
call venv\Scripts\activate

echo 1. Running build script...
python build_deployment.py

echo 2. Checking AWS CLI...
aws --version

echo 3. Deployment commands would run here...
echo (Edit this file with your actual AWS commands)

pause