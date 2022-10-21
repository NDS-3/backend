from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.model import Owner
from app.repository.LetterRepository import LetterRepository
from app.database import get_db

router = APIRouter()

@router.get("/users/{user_id}/letters", tags=["letters"])
async def get_letters(user_id:int,page:int=0, db: Session = Depends(get_db)):
    db_item = LetterRepository.fetch_by_id(db, _id = 1)
    # page로 가져오기
    return {}

@router.post("/users/{user_id}/letters/{letter_id}", tags=["letters"])
async def get_letter_detail():
    return [{
        "lettername": "a"
    },
    {
        "lettername": "b"
    }]

@router.put("/letters/{letter_id}", tags=["letters"])
async def update_letters():

    return {}

@router.delete("/letters/{letter_id}", tags=["letters"])
async def delete_letters():
    return [{
        "lettername": "a"
    },
    {
        "lettername": "b"
    }]

@router.post("/users/{user_id}/letters", tags=["letters"])
async def create_letters():
    return [{
        "lettername": "a"
    },
    {
        "lettername": "b"
    }]