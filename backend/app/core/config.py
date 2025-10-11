from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str = "your-secret-key-here"  # Default value
    JWT_ALGORITHM: str = "HS256"  # Default value

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
