import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

mongo_url = os.getenv("MONGO_URL")
client = MongoClient(mongo_url)
db = client["orders"]  # Usa la base de datos 'orders'
cart_collection = db["carts"]

def add_product_to_order(order_id: str, product_id: str):
    # Intenta buscar por id como string y como número
    query = {"$or": [
        {"id": order_id},
        {"id": int(order_id)} if order_id.isdigit() else {"id": None}
    ]}
    # Elimina la condición inválida si no es número
    query["$or"] = [q for q in query["$or"] if list(q.values())[0] is not None]
    result = cart_collection.update_one(
        query,
        {"$addToSet": {"product_ids": product_id}}
    )
    return result.modified_count > 0
