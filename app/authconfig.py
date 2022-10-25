from pydantic import BaseSettings

class Settings(BaseSettings):
    check_expiration = True
    jwt_header_prefix = "Bearer"
    jwt_header_name = "Authorization"
    userpools = {
        "kr": {
            "region": "ap-northeast-2",
            "userpool_id": "ap-northeast-2_qC6hyIfPz",
            "app_client_id": "1ursigm6o6il7khipt60tdlfb1"
        },
    }

settings = Settings()