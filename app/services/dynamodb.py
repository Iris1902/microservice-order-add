import boto3
import os
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

def add_product_to_order(order_id, product_id):
    response = table.update_item(
        Key={"id": order_id},
        UpdateExpression="SET product_ids = list_append(if_not_exists(product_ids, :empty_list), :p)",
        ExpressionAttributeValues={
            ":p": [product_id],
            ":empty_list": []
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
