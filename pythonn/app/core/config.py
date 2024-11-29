from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Bookly-SENA API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "REST API for Bookly-SENA using FastAPI"
    API_V1_STR: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./bookly.db"
    
    # JWT settings
    SECRET_KEY: str = "your-secret-key"  # Change in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Redis settings
    REDIS_URL: str = "redis://localhost:6379"
    
    class Config:
        env_file = ".env"

settings = Settings()