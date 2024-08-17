from fastapi import APIRouter

router = APIRouter()

@router.get("/route1")
async def route1():
    return {"message": "This is route 1"}