import strawberry
from app.services.dynamodb import create_cart

@strawberry.type
class Cart:
    id: str  # Cambiado a 'id' para coincidir con DynamoDB
    user_id: str
    product_ids: list[str]

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello world"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_cart(self, user_id: str) -> Cart:
        cart_id = create_cart(user_id)
        return Cart(id=cart_id, user_id=user_id, product_ids=[])

schema = strawberry.Schema(query=Query, mutation=Mutation)
