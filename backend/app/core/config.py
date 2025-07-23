import os
from functools import lru_cache
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    PROJECT_NAME: str = "Pinnacle Trust"
    API_VERSION: str = "v1"
    API_PREFIX: str = "/api"
    BASE_URL: str = "http://localhost:8000"

    # Database
    POSTGRES_URL: str
    DATABASE_ECHO: bool = False

    # Auth
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Email (optional)
    SUPPORT_EMAIL: EmailStr = "support@pinnacletrust.com"

    # Environment
    ENV: str = "development"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
