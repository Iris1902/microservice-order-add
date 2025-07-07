from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/order-create/graphql")


@app.get("/order-create/health")
def health():
    return {"status": "ok"}
