from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class BookingCreate(BaseModel):
    hospital_id: int
    doctor_id: Optional[int] = None
    department: str
    patient_name: str
    patient_email: str
    appointment_date: str
    symptoms: Optional[str] = None


@router.post("/")
async def create_booking(booking: BookingCreate):
    return {
        "message": "Booking created successfully",
        "booking_id": 1,
        "status": "pending"
    }


@router.get("/")
async def get_bookings():
    return []


@router.get("/{booking_id}")
async def get_booking(booking_id: int):
    return {"booking_id": booking_id, "status": "pending"}
