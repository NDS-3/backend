from sqlalchemy.orm import Session

from app.model.Owner import Owner
import app.schemas as schemas

class OwnerRepository:
    async def create(db: Session, owner: schemas.OwnerCreate):
        db_item = Owner()
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

        return db_item

    async def fetch_by_id(db: Session, _id:int):
        return db.query(Owner).filter(Owner.id == _id).first()