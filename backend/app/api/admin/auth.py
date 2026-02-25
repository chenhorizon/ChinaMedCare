from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.admin import AdminLogin, Token, AdminResponse
from app.services.auth_service import AuthService
from app.db import get_db

router = APIRouter()


@router.post("/login", response_model=Token)
async def admin_login(credentials: AdminLogin, db: Session = Depends(get_db)):
    """Admin login endpoint"""
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
