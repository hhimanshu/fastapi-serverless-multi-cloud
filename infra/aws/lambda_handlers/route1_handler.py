import json
from mangum import Mangum


def create_app():
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/route1")
    async def root():
        return {"message": "Hello from Route 1"}

    return app


# Initialize the FastAPI app outside the handler
app = create_app()
handler = Mangum(app)


def lambda_handler(event, context):
    return handler(event, context)
