from fastapi import APIRouter, Depends
from datetime import datetime

router = APIRouter()

BASE_DATE = datetime(2022, 11, 11)

@router.get("/days/check", tags=["days"])
async def check_current_date():
    current_date = datetime.now()
    
    is_passed = current_date > BASE_DATE

    return {
        "isPassed": True
    }