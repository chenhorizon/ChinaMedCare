from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    # JWT Settings
    SECRET_KEY: str = os.getenv("JWT_SECRET", "your-super-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Admin credentials (for demo)
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD_HASH: str = os.getenv("ADMIN_PASSWORD_HASH", "")

    class Config:
        env_file = ".env"


settings = Settings()
