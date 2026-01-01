from mangum import Mangum
from app_fgsm import app

handler = Mangum(app)

def lambda_handler(event, context):
    return handler(event, context)