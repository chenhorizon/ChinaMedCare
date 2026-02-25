from fastapi import APIRouter, Query, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from app.db import get_db
from app.services.hospital_service import hospital_service

router = APIRouter()


@router.get("/")
async def get_hospitals(
    department: Optional[str] = None,
    city: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get all hospitals with filters (public endpoint)"""
    result = hospital_service.get_hospitals(
        db=db,
        page=1,
        page_size=100,  # Return up to 100 hospitals for public view
        search=search,
        department=department,
        city=city
    )
    return result.items


@router.get("/{hospital_id}")
async def get_hospital(hospital_id: int, db: Session = Depends(get_db)):
    """Get a single hospital by ID (public endpoint)"""
    hospital = hospital_service.get_hospital_by_id(db, hospital_id)
    if hospital:
        return hospital
    return {"error": "Hospital not found"}
