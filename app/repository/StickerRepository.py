from sqlalchemy.orm import Session

from app.model.Sticker import Sticker
import app.schemas as schemas

class StickerRepository:
    async def fetch_all(db: Session):
        return db.query(Sticker).all()

    async def fetch_by_id(db: Session, _id:int):
        db_sticker = db.query(Sticker).filter(Sticker.id == _id).first()

        if not db_sticker:
            raise HTTPException(status_code=400, detail="Sticker not found")

        return db_sticker