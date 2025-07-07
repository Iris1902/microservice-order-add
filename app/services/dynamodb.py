import boto3
import os
import random
from dotenv import load_dotenv
load_dotenv()

dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

def create_cart(user_id):
    cart_id = random.randint(1_000_000, 9_999_999) 
    table.put_item(
        Item={
            "id": cart_id, 
            "user_id": user_id,
            "product_ids": []
        }
    )
    return cart_id
