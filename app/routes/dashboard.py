from fastapi import APIRouter, Depends
from app.utils.jwt import decode_access_token

router = APIRouter()

@router.get("/")
async def get_dashboard_data(token: str = Depends(decode_access_token)):
    return {"data": "Welcome to the dashboard!"}
