from pydantic import BaseModel, Field
from typing import List, Optional


class HospitalBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    location: str = Field(..., min_length=1, max_length=200)
    rating: float = Field(..., ge=0.0, le=5.0)
    image: str = Field(..., min_length=1)
    departments: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)


class HospitalCreate(HospitalBase):
    pass


class HospitalUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    location: Optional[str] = Field(None, min_length=1, max_length=200)
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)
    image: Optional[str] = None
    departments: Optional[List[str]] = None
    languages: Optional[List[str]] = None


class Hospital(HospitalBase):
    id: int

    class Config:
        from_attributes = True


class PaginatedHospitalResponse(BaseModel):
    items: List[Hospital]
    total: int
    page: int
    page_size: int
    total_pages: int
