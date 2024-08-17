from mangum import Mangum
from fastapi import FastAPI
from app.routes import route2

app = FastAPI()
app.include_router(route2.router)

handler = Mangum(app)