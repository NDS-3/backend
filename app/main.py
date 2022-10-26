from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI

from app.router import users, letters, stickers
from app.database import engine, Base

from starlette.middleware.cors import CORSMiddleware
from fastapi_cognito import CognitoAuth, CognitoSettings
from app.authconfig import settings

# default userpool(eu) will be used if there is no userpool_name param provided.

origins = [
    "http://localhost:3000",
    "http://localhost"
]

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI()

    Base.metadata.create_all(bind=engine)

    # 미들웨어 정의
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

    # 라우터 정의
    app.include_router(users.router)
    app.include_router(letters.router)
    app.include_router(stickers.router)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)