from sqlalchemy.orm import Session
from datetime import datetime
from app.model.Letter import Letter
import app.schemas as schemas

class LetterRepository:
    async def create(db: Session, letter: schemas.LetterCreate):
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

    async def fetch_by_id(db: Session, _id:int):
        return db.query(Letter).filter(Letter.id == _id).first()