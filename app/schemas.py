from typing import List, Optional, Union

from pydantic import BaseModel

class StickerBase(BaseModel):
    image_url: str

class Sticker(StickerBase):
    id: int

    class Config:
        orm_mode = True

class StickerCreate(StickerBase):
    pass

class LetterBase(BaseModel):
    owner_id : int
    sticker_id : int
    content : str
    password : str

class Letter(LetterBase):
    id: int

    class Config:
        orm_mode = True

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