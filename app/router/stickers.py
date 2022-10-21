from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repository.CharacterRepository import CharacterRepository
from app.database import get_db

router = APIRouter()

@router.get("/stickers", tags=["stickers"])
async def get_stickers(db: Session = Depends(get_db)):
    stcikers =  await CharacterRepository.fetch_all(db=db)

    return stcikers