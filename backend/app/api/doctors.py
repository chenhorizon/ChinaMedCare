from fastapi import APIRouter

router = APIRouter()

doctors_data = [
    {
        "id": 1,
        "name": "Dr. Zhang Wei",
        "title": "Chief Physician",
        "specialty": "Cardiology",
        "hospital": "Peking Union Medical College Hospital",
        "languages": ["Chinese", "English"],
        "rating": 4.9
    }
]


@router.get("/")
async def get_doctors():
    return doctors_data


@router.get("/{doctor_id}")
async def get_doctor(doctor_id: int):
    doctor = next((d for d in doctors_data if d["id"] == doctor_id), None)
    if doctor:
        return doctor
    return {"error": "Doctor not found"}
