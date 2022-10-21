from sqlalchemy import Column, ForeignKey, DateTime, Integer, String, Float, Boolean

from app.database import Base


class Letter(Base):
    __tablename__ = "letters"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    owner_id = Column(Integer, ForeignKey("owners.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))
    content = Column(String(500), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=True)
    modified_at = Column(DateTime, nullable=True)