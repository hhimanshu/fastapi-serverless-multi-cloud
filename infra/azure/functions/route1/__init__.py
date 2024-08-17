import azure.functions as func
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes import route1

app = FastAPI()
app.include_router(route1.router)

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    request = {
        "method": req.method,
        "url": str(req.url),
        "headers": dict(req.headers),
        "params": dict(req.params),
        "body": req.get_body().decode()
    }
    
    from fastapi.encoders import jsonable_encoder
    from starlette.responses import Response
    
    response = await app.router(scope={
        "type": "http",
        "httpMethod": request["method"],
        "path": request["url"].split("/api")[1],
        "headers": request["headers"]
    }, receive=None)
    
    func_response = func.HttpResponse(
        body=response.body,
        status_code=response.status_code,
        headers=dict(response.headers)
    )
    
    return func_response