# test_lambda.py
import json
from lambda_handler import lambda_handler

def test_lambda_handler():
    """Test the Lambda handler with a mock API Gateway event"""
    
    # Mock API Gateway event
    mock_event = {
        "version": "2.0",
        "routeKey": "ANY /{proxy+}",
        "rawPath": "/health",
        "rawQueryString": "",
        "headers": {
            "content-type": "application/json"
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "api-id",
            "domainName": "id.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "id",
            "http": {
                "method": "GET",
                "path": "/health",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1",
                "userAgent": "test-agent"
            },
            "requestId": "request-id",
            "routeKey": "ANY /{proxy+}",
            "stage": "$default",
            "time": "12/Mar/2024:19:45:18 +0000",
            "timeEpoch": 1647114318000
        },
        "isBase64Encoded": False
    }
    
    print("Testing Lambda handler...")
    print(f"Event path: {mock_event['rawPath']}")
    
    try:
        # Call the handler
        response = lambda_handler(mock_event, None)
        
        print("\n✅ Lambda handler executed successfully!")
        print(f"Status Code: {response.get('statusCode', 'No status')}")
        print(f"Response Body: {response.get('body', 'No body')[:200]}...")
        
        if response.get('statusCode') == 200:
            print("\n✅ Test PASSED!")
        else:
            print("\n⚠ Test completed but status code not 200")
            
    except Exception as e:
        print(f"\n❌ Test FAILED: {str(e)}")

if __name__ == "__main__":
    test_lambda_handler()