from sqlalchemy import Column, Integer, String, Float, Boolean

from app.database import Base


class Sticker(Base):
    __tablename__ = "stickers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    image_url = Column(String(255), nullable=False)