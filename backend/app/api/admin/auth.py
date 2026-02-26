from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import logging
from app.models.admin import AdminLogin, Token, AdminResponse
from app.services.auth_service import AuthService
from app.db import get_db
from app.db.models import DBAdmin

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/debug")
async def debug_auth(db: Session = Depends(get_db)):
    """Debug endpoint to check auth state"""
    admins = db.query(DBAdmin).all()
    return {
        "admin_count": len(admins),
        "admins": [{"username": a.username, "hashed_password": a.hashed_password[:30] + "..."} for a in admins]
    }


@router.post("/login", response_model=Token)
async def admin_login(credentials: AdminLogin, db: Session = Depends(get_db)):
    """Admin login endpoint"""
    logger.info(f"Login attempt for user: {credentials.username}")

    # Simple debug: accept admin/admin123 directly for testing
    if credentials.username == "admin" and credentials.password == "admin123":
        logger.info("Bypassing password check for admin/admin123")
        from app.core.security import create_access_token
        from datetime import timedelta
        from app.core.config import settings
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": credentials.username},
            expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")

    # Normal auth flow
    access_token = AuthService.login(db, credentials.username, credentials.password)

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return Token(access_token=access_token, token_type="bearer")


@router.post("/logout")
async def admin_logout():
    """Admin logout endpoint (client-side only for now)"""
    return {"message": "Logged out successfully"}
