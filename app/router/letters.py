from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model import Letter
from app.schemas import Letter, LetterDetail
from app.repository.LetterRepository import LetterRepository
from app.repository.OwnerRepository import OwnerRepository
from app.repository.StickerRepository import StickerRepository
from app.database import get_db
from passlib.hash import pbkdf2_sha256 as password_encoder
from fastapi_utils.camelcase import camel2snake, snake2camel

router = APIRouter()

@router.get("/users/{user_id}/letters", tags=["letters"])
async def get_letters(user_id: int, page: int=0, db: Session = Depends(get_db)):
    db_letter = await LetterRepository.fetch_by_id(db, _id = user_id)
    # page로 가져오기
    return db_letter

@router.post("/users/{user_id}/letters/{letter_id}", tags=["letters"], response_model=LetterDetail, response_model_exclude_none=True)
async def get_letter_detail(user_id: int, letter_id: int, letter: Letter, db: Session = Depends(get_db)):
    db_letter = await LetterRepository.fetch_by_id(db, _id=letter_id)
    incorrect_password = not password_encoder.verify(letter.password, db_letter.password)

    if incorrect_password:
        raise HTTPException(status_code=403, detail='Incorrect Password')

    sticker = await StickerRepository.fetch_by_id(db, _id=db_letter.sticker_id)
    response_letter = LetterDetail(id=db_letter.id, sticker=sticker, content=db_letter.content)

    return response_letter

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

@router.post("/users/{user_id}/letters", tags=["letters"], response_model=LetterDetail, response_model_exclude_none=True)
async def create_letters(user_id: int, letter: Letter, db: Session = Depends(get_db)):
    owner = await OwnerRepository.fetch_by_id(db, user_id)
    
    setattr(letter, 'owner_id', user_id)
    hash_value = password_encoder.hash(letter.password)
    setattr(letter, 'password', hash_value)
    db_letter = await LetterRepository.create(db, letter)
    sticker = await StickerRepository.fetch_by_id(db, _id=db_letter.sticker_id)

    response_letter = LetterDetail(id=db_letter.id, sticker=sticker, content=db_letter.content)
    return response_letter