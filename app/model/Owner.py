from sqlalchemy import Column, Integer, String, Float, Boolean

from app.database import Base


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    email = Column(String(255), nullable=False)
    username = Column(String(255), nullable=True)
    personal_url = Column(String(255), nullable=True)

    def exists_url(self):
        return self.personal_url is not None