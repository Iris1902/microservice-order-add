import strawberry
from app.services.dynamodb import add_product_to_order

@strawberry.type
class Order:
    id: str
    product_ids: list[str]

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello world"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_product_to_order(self, order_id: str, product_id: str) -> bool:
        return add_product_to_order(order_id, product_id)

schema = strawberry.Schema(query=Query, mutation=Mutation)
