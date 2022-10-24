from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI

from .router import users, letters, stickers
from app.database import engine, Base

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI()

    Base.metadata.create_all(bind=engine)

    # 라우터 정의
    app.include_router(users.router)
    app.include_router(letters.router)
    app.include_router(stickers.router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)