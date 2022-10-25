from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field

class StickerBase(BaseModel):
    image_url: Union[str, None] = Field(default=None, alias='imageUrl')

class Sticker(StickerBase):
    id: Union[int, None]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

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
        allow_population_by_field_name = True

class LetterModify(LetterBase):
    id: Union[int, None] = Field(default=None, alias='letterId')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
    

class LetterDetail(LetterBase):
    id: Union[int, None]
    sticker: Union[Sticker, None]

class LetterCreate(LetterBase):
    pass

class OwnerBase(BaseModel):
    email: Union[str, None]
    username: Union[str, None]
    personal_url: Union[str, None] = Field(default=None, alias='personalUrl')

class Owner(OwnerBase):
    id: Union[int, None]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class OwnerCreate(OwnerBase):
    pass