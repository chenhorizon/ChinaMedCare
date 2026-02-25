from datetime import timedelta
from typing import Optional
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.security import (
    verify_password,
    create_access_token,
    DEFAULT_ADMIN_HASH
)
from app.db.models import DBAdmin


class AuthService:
    """Service layer for authentication with database"""

    @classmethod
    def get_admin(cls, db: Session, username: str) -> Optional[DBAdmin]:
        """Get admin by username from database"""
        return db.query(DBAdmin).filter(DBAdmin.username == username).first()

    @classmethod
    def authenticate_admin(cls, db: Session, username: str, password: str) -> bool:
        """Authenticate admin credentials against database"""
        admin = cls.get_admin(db, username)
        if admin:
            return verify_password(password, admin.hashed_password)
        # Fallback to default admin if no admin in DB
        if username == settings.ADMIN_USERNAME:
            return verify_password(password, DEFAULT_ADMIN_HASH)
        return False

    @classmethod
    def login(cls, db: Session, username: str, password: str) -> Optional[str]:
        """Login and return access token"""
        if not cls.authenticate_admin(db, username, password):
            return None

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": username},
            expires_delta=access_token_expires
        )
        return access_token

    @classmethod
    def ensure_admin_exists(cls, db: Session):
        """Ensure default admin exists in database"""
        admin = cls.get_admin(db, settings.ADMIN_USERNAME)
        if not admin:
            # Create default admin
            admin = DBAdmin(
                username=settings.ADMIN_USERNAME,
                hashed_password=DEFAULT_ADMIN_HASH
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
