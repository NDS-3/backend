from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model import Owner
from app.repository.OwnerRepository import OwnerRepository
from app.database import get_db
from app.schemas import Owner
from operator import attrgetter
from secrets import token_urlsafe
from app.authconfig import settings
from fastapi_cognito import CognitoToken, CognitoAuth, CognitoSettings

router = APIRouter()
cognito_kr = CognitoAuth(settings=CognitoSettings.from_global_settings(settings), userpool_name="kr")

@router.get("/users/{url}", tags=["users"], response_model=Owner, response_model_exclude_none=True)
async def get_users(url:str, db: Session = Depends(get_db)):
    owner = await OwnerRepository.fetch_by_url(db, url)

    setattr(owner, 'personal_url', None)
    setattr(owner, 'email', None)

    return owner

@router.patch("/users/me", tags=["users"], response_model=Owner)
async def update_users(owner: Owner, auth: CognitoToken = Depends(cognito_kr.auth_required), db: Session = Depends(get_db)):
    if owner.id is None or owner.username is None:
        raise HTTPException(status_code=400, detail="id, username이 필요합니다.")
        
    return await OwnerRepository.update_username(db, owner, auth)

@router.get("/users/me/encryption", tags=["users"], response_model=Owner, response_model_exclude_none=True)
async def get_users_url(auth: CognitoToken = Depends(cognito_kr.auth_required), db: Session = Depends(get_db)):
    owner = await OwnerRepository.get_user(db, auth)

    if owner.exists_url():
        setattr(owner, 'id', None)
        setattr(owner, 'email', None)

        return owner

    setattr(owner, 'personal_url', token_urlsafe(16))

    return await OwnerRepository.update_personal_url(db, owner)

@router.get("/test")
async def test(auth: CognitoToken = Depends(cognito_kr.auth_required)):
    print(auth.username)
    return {"message": "Hello world"}