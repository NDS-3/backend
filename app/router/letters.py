from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from app.model import Letter
from app.schemas import Letter, LetterDetail, LetterModify
from app.repository.LetterRepository import LetterRepository
from app.repository.OwnerRepository import OwnerRepository
from app.repository.StickerRepository import StickerRepository
from app.database import get_db
from passlib.hash import pbkdf2_sha256 as password_encoder
from fastapi_utils.camelcase import camel2snake, snake2camel
from typing import List

router = APIRouter()

@router.get("/users/{user_id}/letters", tags=["letters"], response_model=List, response_model_exclude_none=True)
async def get_letters(user_id: int, page: int=0, db: Session = Depends(get_db)):
    db_letter_list = await LetterRepository.fetch_all(db, owner_id=user_id, page=page)
    # page로 가져오기
    result = []
    for db_letter in db_letter_list:
        result.append(await convertLetterDetail(db, db_letter))

    return result[page*10:(page+1)*10]

async def convertLetterDetail(db, letter: Letter):
    sticker = await StickerRepository.fetch_by_id(db, _id=letter.sticker_id)
    response_letter = LetterDetail(id=letter.id, sticker=sticker, content=letter.content)

    return response_letter

@router.post("/users/{user_id}/letters/{letter_id}", tags=["letters"], response_model=LetterDetail, response_model_exclude_none=True)
async def get_letter_detail(user_id: int, letter_id: int, letter: Letter, db: Session = Depends(get_db)):
    db_letter = await LetterRepository.fetch_by_id(db, _id=letter_id)
    incorrect_password = not password_encoder.verify(letter.password, db_letter.password)

    if incorrect_password:
        raise HTTPException(status_code=403, detail='Incorrect Password')

    sticker = await StickerRepository.fetch_by_id(db, _id=db_letter.sticker_id)
    response_letter = LetterDetail(id=db_letter.id, sticker=sticker, content=db_letter.content)

    return response_letter

@router.patch("/letters/{letter_id}", tags=["letters"], response_model=LetterDetail, response_model_exclude_none=True)
async def update_letters(letter: LetterModify, db: Session = Depends(get_db)):
    db_letter = await LetterRepository.update(db, letter)
    sticker = await StickerRepository.fetch_by_id(db, _id=db_letter.sticker_id)

    response_letter = LetterDetail(id=db_letter.id, sticker=sticker, content=db_letter.content)

    return response_letter

@router.delete("/letters/{letter_id}", tags=["letters"])
async def delete_letters(letter_id: int, db: Session = Depends(get_db)):
    db_letter = await LetterRepository.fetch_by_id(db, _id=letter_id)
    await LetterRepository.delete(db, db_letter)

    return Response(status_code=HTTP_204_NO_CONTENT)

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