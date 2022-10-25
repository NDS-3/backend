from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repository.StickerRepository import StickerRepository
from app.database import get_db
from app.schemas import Sticker
from typing import List

router = APIRouter()

@router.get("/stickers", tags=["stickers"], response_model=List[Sticker])
async def get_stickers(db: Session = Depends(get_db)):
    stickers =  await StickerRepository.fetch_all(db=db)

    return stickers