from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field

class StickerBase(BaseModel):
    image_url: str

class Sticker(StickerBase):
    id: int

    class Config:
        orm_mode = True

class StickerCreate(StickerBase):
    pass

class LetterBase(BaseModel):
    owner_id : Union[int, None] = Field(default=None, alias='ownerId')
    sticker_id : Union[int, None] = Field(default=None, alias='stickerId')
    content : Union[str, None]
    password : Union[str, None]
    created_at : Union[datetime, None]
    modified_at : Union[datetime, None]

class Letter(LetterBase):
    id: Union[int, None]

    class Config:
        orm_mode = True

class LetterModify(LetterBase):
    id: Union[int, None] = Field(default=None, alias='letterId')

    class Config:
        orm_mode = True
    

class LetterDetail(LetterBase):
    id: Union[int, None]
    sticker: Union[Sticker, None]

class LetterCreate(LetterBase):
    pass

class OwnerBase(BaseModel):
    email: Union[str, None]
    username: Union[str, None]
    personal_url: Union[str, None]

class Owner(OwnerBase):
    id: Union[int, None]

    class Config:
        orm_mode = True

class OwnerCreate(OwnerBase):
    pass