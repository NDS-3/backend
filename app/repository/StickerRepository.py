from sqlalchemy.orm import Session

from app.model.Sticker import Sticker
import app.schemas as schemas

class StickerRepository:
    async def fetch_all(db: Session):
        return db.query(Sticker).all()