@echo off
echo ======================================
echo   FGSM PROJECT - SCREENSHOT GUIDE
echo ======================================
echo.
echo STEP 1: Make sure both servers are running:
echo   1. Backend: http://localhost:8000
echo   2. Frontend: http://localhost:3000
echo.
echo STEP 2: Take these 5 screenshots:
echo.
echo [1] FRONTEND UI
echo    URL: http://localhost:3000
echo    What to show: Epsilon slider, Upload button
echo.
echo [2] BACKEND API DOCS
echo    URL: http://localhost:8000/docs
echo    What to show: All API endpoints
echo.
echo [3] WORKING ADVERSARIAL EXAMPLE
echo    URL: http://localhost:3000
echo    Steps: Upload image, click Generate
echo    What to show: Original & adversarial images + predictions
echo.
echo [4] TERMINALS RUNNING
echo    Show BOTH Command Prompt windows:
echo    - Backend: "Application startup complete"
echo    - Frontend: "Next.js ready on localhost:3000"
echo.
echo [5] FILE STRUCTURE
echo    Open File Explorer to: D:\FGSM
echo    Show: deployment_package.zip and all Python files
echo.
echo STEP 3: Save screenshots to:
echo    D:\FGSM\screenshots\
echo    Names: screenshot1.png, screenshot2.png, etc.
echo.
echo STEP 4: Create submission package:
echo    cd D:\FGSM
echo    powershell "Compress-Archive DEPLOYMENT_REPORT.md screenshots deployment_package.zip -DestinationPath submission.zip"
echo.
echo PRESS ANY KEY TO CONTINUE...
pause > nul