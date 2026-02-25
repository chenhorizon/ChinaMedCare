from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Optional
from sqlalchemy.orm import Session
from app.models.hospital import (
    Hospital,
    HospitalCreate,
    HospitalUpdate,
    PaginatedHospitalResponse
)
from app.services.hospital_service import hospital_service
from app.core.dependencies import get_current_admin
from app.db import get_db

router = APIRouter()


@router.get("", response_model=PaginatedHospitalResponse)
async def get_admin_hospitals(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Search by name"),
    department: Optional[str] = Query(None, description="Filter by department"),
    city: Optional[str] = Query(None, description="Filter by city"),
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    """Get paginated list of hospitals (admin only)"""
    return hospital_service.get_hospitals(
        db=db,
        page=page,
        page_size=page_size,
        search=search,
        department=department,
        city=city
    )


@router.get("/{hospital_id}", response_model=Hospital)
async def get_admin_hospital(
    hospital_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    """Get a single hospital by ID (admin only)"""
    hospital = hospital_service.get_hospital_by_id(db, hospital_id)
    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hospital not found"
        )
    return hospital


@router.post("", response_model=Hospital, status_code=status.HTTP_201_CREATED)
async def create_admin_hospital(
    hospital: HospitalCreate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    """Create a new hospital (admin only)"""
    return hospital_service.create_hospital(db, hospital)


@router.put("/{hospital_id}", response_model=Hospital)
async def update_admin_hospital(
    hospital_id: int,
    hospital_update: HospitalUpdate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    """Update an existing hospital (admin only)"""
    hospital = hospital_service.update_hospital(db, hospital_id, hospital_update)
    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hospital not found"
        )
    return hospital


@router.delete("/{hospital_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_admin_hospital(
    hospital_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    """Delete a hospital (admin only)"""
    deleted = hospital_service.delete_hospital(db, hospital_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hospital not found"
        )
    return None
