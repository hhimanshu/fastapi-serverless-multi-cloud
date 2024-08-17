from mangum import Mangum
from fastapi import FastAPI
from app.routes import route1

app = FastAPI()
app.include_router(route1.router)

handler = Mangum(app)