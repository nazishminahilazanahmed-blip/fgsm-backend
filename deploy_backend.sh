#!/bin/bash
# backend/deploy_backend.sh

echo "Building backend for AWS Lambda..."

# Install dependencies locally first
pip install -r requirements.txt

# Create deployment package
python build_deployment.py

# Check package size
SIZE=$(ls -lh deployment_package.zip | awk '{print $5}')
echo "Package size: $SIZE"

# Instructions for manual upload
echo ""
echo "=== DEPLOYMENT INSTRUCTIONS ==="
echo "1. Go to AWS Lambda Console"
echo "2. Create new function with Python 3.9 runtime"
echo "3. Upload deployment_package.zip"
echo "4. Set handler to: lambda_handler.lambda_handler"
echo "5. Set timeout to at least 30 seconds"
echo "6. Create API Gateway trigger"
echo "==============================="