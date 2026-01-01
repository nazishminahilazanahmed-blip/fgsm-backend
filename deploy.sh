#!/bin/bash
# deploy.sh

echo "=========================================="
echo "AWS Lambda Deployment Script"
echo "=========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Step 1: Checking files...${NC}"
if [ ! -f "app_fgsm.py" ]; then
    echo -e "${RED}✗ app_fgsm.py not found${NC}"
    exit 1
fi

if [ ! -f "lambda_handler.py" ]; then
    echo -e "${RED}✗ lambda_handler.py not found${NC}"
    exit 1
fi

echo -e "${GREEN}✓ All required files found${NC}"

echo -e "\n${YELLOW}Step 2: Creating deployment package...${NC}"
python build_deployment.py

if [ $? -ne 0 ]; then
    echo -e "${RED}✗ Failed to create deployment package${NC}"
    exit 1
fi

echo -e "\n${YELLOW}Step 3: Testing locally...${NC}"
python -c "from lambda_handler import lambda_handler; print('✓ Lambda handler imports successfully')"

echo -e "\n${GREEN}✅ Ready for AWS deployment!${NC}"
echo -e "\n${YELLOW}Next steps:${NC}"
echo "1. Go to AWS Lambda Console"
echo "2. Create new function (Python 3.9)"
echo "3. Upload deployment_package.zip"
echo "4. Set handler to: lambda_handler.lambda_handler"
echo "5. Set timeout to 30 seconds"
echo "6. Create API Gateway trigger"
echo -e "\n${YELLOW}Quick test command:${NC}"
echo "python test_lambda.py"