from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    check_expiration = True
    jwt_header_prefix = "Bearer"
    jwt_header_name = "Authorization"
    userpools = {
        "kr": {
            "region": os.environ.get('AWS_REGION'),
            "userpool_id": os.environ.get('AWS_COGNITO_USERPOOL_ID'),
            "app_client_id": os.environ.get('AWS_COGNITO_APP_CLIENT_ID')
        },
    }

settings = Settings()