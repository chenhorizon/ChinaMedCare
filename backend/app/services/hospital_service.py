from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from app.models.hospital import Hospital, HospitalCreate, HospitalUpdate, PaginatedHospitalResponse
from app.db.models import DBHospital


class HospitalService:
    """Service layer for hospital operations with database"""

    @staticmethod
    def _to_pydantic(db_hospital: DBHospital) -> Hospital:
        """Convert DB model to Pydantic model"""
        return Hospital(
            id=db_hospital.id,
            name=db_hospital.name,
            location=db_hospital.location,
            rating=db_hospital.rating,
            image=db_hospital.image,
            departments=db_hospital.departments or [],
            languages=db_hospital.languages or []
        )

    @staticmethod
    def get_hospitals(
        db: Session,
        page: int = 1,
        page_size: int = 10,
        search: Optional[str] = None,
        department: Optional[str] = None,
        city: Optional[str] = None
    ) -> PaginatedHospitalResponse:
        """Get paginated list of hospitals from database"""
        # Build query
        query = db.query(DBHospital)

        # Get all hospitals first, then filter in Python for better control
        all_hospitals = query.all()

        # Apply filters in Python
        filtered_hospitals = all_hospitals

        # Search filter: search in name, location, and departments
        if search:
            search_lower = search.lower()
            filtered_hospitals = [
                h for h in filtered_hospitals
                if (h.name and search_lower in h.name.lower())
                or (h.location and search_lower in h.location.lower())
                or (h.departments and any(search_lower in dept.lower() for dept in h.departments))
            ]

        # City filter
        if city:
            city_lower = city.lower()
            filtered_hospitals = [
                h for h in filtered_hospitals
                if h.location and city_lower in h.location.lower()
            ]

        # Department filter (case-insensitive)
        if department:
            dept_lower = department.lower()
            filtered_hospitals = [
                h for h in filtered_hospitals
                if h.departments and any(dept_lower == d.lower() for d in h.departments)
            ]

        # Get total count after filtering
        total = len(filtered_hospitals)

        # Apply pagination
        offset = (page - 1) * page_size
        paginated_hospitals = filtered_hospitals[offset : offset + page_size]

        # Convert to Pydantic models
        items = [HospitalService._to_pydantic(h) for h in paginated_hospitals]
        total_pages = (total + page_size - 1) // page_size if total > 0 else 0

        return PaginatedHospitalResponse(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    @staticmethod
    def get_hospital_by_id(db: Session, hospital_id: int) -> Optional[Hospital]:
        """Get hospital by ID from database"""
        db_hospital = db.query(DBHospital).filter(DBHospital.id == hospital_id).first()
        if db_hospital:
            return HospitalService._to_pydantic(db_hospital)
        return None

    @staticmethod
    def create_hospital(db: Session, hospital_create: HospitalCreate) -> Hospital:
        """Create a new hospital in database"""
        db_hospital = DBHospital(
            name=hospital_create.name,
            location=hospital_create.location,
            rating=hospital_create.rating,
            image=hospital_create.image,
            departments=hospital_create.departments,
            languages=hospital_create.languages
        )
        db.add(db_hospital)
        db.commit()
        db.refresh(db_hospital)
        return HospitalService._to_pydantic(db_hospital)

    @staticmethod
    def update_hospital(db: Session, hospital_id: int, hospital_update: HospitalUpdate) -> Optional[Hospital]:
        """Update an existing hospital in database"""
        db_hospital = db.query(DBHospital).filter(DBHospital.id == hospital_id).first()
        if not db_hospital:
            return None

        # Update only provided fields
        update_data = hospital_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_hospital, field, value)

        db.commit()
        db.refresh(db_hospital)
        return HospitalService._to_pydantic(db_hospital)

    @staticmethod
    def delete_hospital(db: Session, hospital_id: int) -> bool:
        """Delete a hospital from database"""
        db_hospital = db.query(DBHospital).filter(DBHospital.id == hospital_id).first()
        if db_hospital:
            db.delete(db_hospital)
            db.commit()
            return True
        return False


# Global service instance
hospital_service = HospitalService()
