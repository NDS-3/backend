from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.model.Letter import Letter
import app.schemas as schemas

class LetterRepository:
    async def create(db: Session, letter: schemas.LetterCreate):
        letter_list = await LetterRepository.fetch_all(db, letter.owner_id)
        
        if len(letter_list) >= 30:
            raise HTTPException(status_code=400, detail="한 사람당 편지의 개수는 30개로 제한됩니다.")

        db_letter = Letter(
            owner_id=letter.owner_id,
            sticker_id=letter.sticker_id,
            content=letter.content,
            password=letter.password
            )
        db.add(db_letter)
        db.commit()
        db.refresh(db_letter)

        setattr(db_letter, 'password', None)

        return db_letter

    async def fetch_all(db: Session, owner_id: int):
        db_letter_list = db.query(Letter).filter(Letter.owner_id == owner_id).all()

        return db_letter_list
    
    async def update(db: Session, letter: schemas.LetterModify):
        db_letter = await LetterRepository.fetch_by_id(db, letter.id)

        setattr(db_letter, 'sticker_id', letter.sticker_id)
        setattr(db_letter, 'content', letter.content)
        setattr(db_letter, 'modified_at', datetime.now())

        db.commit()
        db.refresh(db_letter)

        return db_letter

    async def delete(db: Session, letter: schemas.Letter):
        db.delete(letter)
        db.commit()

    async def fetch_by_id(db: Session, _id:int):
        db_letter = db.query(Letter).filter(Letter.id == _id).first()

        if not db_letter:
            raise HTTPException(status_code=400, detail="Letter not found")

        return db.query(Letter).filter(Letter.id == _id).first()