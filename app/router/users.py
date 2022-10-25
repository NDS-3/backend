from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model import Owner
from app.repository.OwnerRepository import OwnerRepository
from app.database import get_db
from app.schemas import Owner
from operator import attrgetter
from secrets import token_urlsafe

router = APIRouter()

@router.get("/users/{url}", tags=["users"], response_model=Owner, response_model_exclude_none=True)
async def get_users(url:str, db: Session = Depends(get_db)):
    owner = await OwnerRepository.fetch_by_url(db, url)

    setattr(owner, 'personal_url', None)
    setattr(owner, 'email', None)

    return owner

@router.patch("/users/{user_id}", tags=["users"])
async def update_users(user_id:int, owner: Owner, db: Session = Depends(get_db)):
    if owner.id is None or owner.username is None:
        raise HTTPException(status_code=400, detail="id, username이 필요합니다.")
        
    return await OwnerRepository.update_username(db, owner)

@router.get("/users/{user_id}/encryption", tags=["users"], response_model=Owner, response_model_exclude_none=True)
async def get_users_url(user_id:int, db: Session = Depends(get_db)):
    owner = await OwnerRepository.fetch_by_id(db, user_id)

    if owner.exists_url:
        setattr(owner, 'id', None)
        setattr(owner, 'email', None)
        
        return owner

    setattr(owner, 'personal_url', token_urlsafe(16))

    return await OwnerRepository.update_personal_url(db, owner)