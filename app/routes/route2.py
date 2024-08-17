from fastapi import APIRouter

router = APIRouter()

@router.get("/route2")
async def route2():
    return {"message": "This is route 2"}