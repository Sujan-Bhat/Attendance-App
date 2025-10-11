# backend/app/core/config.py
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # App metadata
    PROJECT_NAME: str = "Attendance API"
    PROJECT_VERSION: str = "0.0.1"

    # Database (required) - no default so it fails loudly if not set
    DATABASE_URL: str

    # Redis / broker
    REDIS_URL: str = "redis://redis:6379/0"

    # Security / tokens
    JWT_SECRET_KEY: str = "your-secret-key-here"
    JWT_ALGORITHM: str = "HS256"

    # QR signing secret and TTL
    HMAC_QR_SECRET: str = "qr-secret-default"
    QR_TTL_SECONDS: int = 600  # QR token lifetime in seconds (default 10 minutes)

    # Optional Sentry / storage
    SENTRY_DSN: Optional[str] = None
    S3_ENDPOINT: Optional[str] = None
    S3_BUCKET: Optional[str] = None
    S3_ACCESS_KEY: Optional[str] = None
    S3_SECRET_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# instantiate settings (reads .env if present)
settings = Settings()

# convenience alias used by some modules
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
