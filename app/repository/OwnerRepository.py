from sqlalchemy.orm import Session
from sqlalchemy import update
from app.model.Owner import Owner
from fastapi import HTTPException
import app.schemas as schemas

class OwnerRepository:
    async def create(db: Session, owner: schemas.OwnerCreate):
        db_item = Owner()
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

        return db_item

    async def update_username(db: Session, owner: schemas.Owner):
        db_owner = db.get(Owner, owner.id)

        if not db_owner:
            raise HTTPException(status_code=400, detail="Owner not found")

        setattr(db_owner, "username", owner.username)
        db.commit()
        db.refresh(db_owner)

        return db_owner
    
    async def update_personal_url(db: Session, owner: schemas.Owner):
        db_owner = db.get(Owner, owner.id)

        if not db_owner:
            raise HTTPException(status_code=400, detail="Owner not found")
        
        setattr(db_owner, "personal_url", owner.personal_url)
        db.commit()
        db.refresh(db_owner)

        return db_owner

    async def fetch_by_id(db: Session, _id:int):
        db_owner = db.query(Owner).filter(Owner.id == _id).first()

        if not db_owner:
            raise HTTPException(status_code=400, detail="Owner not found")

        return db_owner
    
    async def fetch_by_url(db: Session, url: str):
        db_owner = db.query(Owner).filter(Owner.personal_url == url).first()

        if not db_owner:
            raise HTTPException(status_code=400, detail="Owner not found")

        return db_owner