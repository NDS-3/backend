from sqlalchemy.orm import Session

from app.model.Letter import Letter
import app.schemas as schemas

class LetterRepository:
    async def create(db: Session, character: schemas.LetterCreate):
        db_item = Letter()
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

        return db_item

    async def fetch_by_id(db: Session, _id:int):
        return db.query(Letter).filter(Letter.id == _id).first()