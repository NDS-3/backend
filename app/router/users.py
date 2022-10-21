from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.model import Owner
from app.repository.CharacterRepository import CharacterRepository
from app.database import get_db

router = APIRouter()

@router.get("/users/{user_id}", tags=["users"])
async def get_users(user_id:int, db: Session = Depends(get_db)):
    db_item = CharacterRepository.fetch_by_id(db, _id = 1)

    return await CharacterRepository.create(db=db, character={
        "image_url":"sdasd"
    })

@router.get("/users/{user_id}/encryption", tags=["users"])
async def get_users_url(db: Session = Depends(get_db)):
    return [{
        "username": "a"
    },
    {
        "username": "b"
    }]

@router.get("/stickers", tags=["stickers"])
async def get_stickers(db: Session = Depends(get_db)):
    stcikers =  await CharacterRepository.fetch_all(db=db)

    return stcikers