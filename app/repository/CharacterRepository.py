from sqlalchemy.orm import Session

from app.model.Character import Character
import app.schemas as schemas

class CharacterRepository:
    async def fetch_all(db: Session):
        return db.query(Character).all()