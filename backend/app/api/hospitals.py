from fastapi import APIRouter, Query
from typing import List, Optional

router = APIRouter()

# Mock data
hospitals_data = [
    {
        "id": 1,
        "name": "Peking Union Medical College Hospital",
        "location": "Beijing, China",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400",
        "departments": ["Cardiology", "Neurology", "Oncology", "Orthopedics"],
        "languages": ["English", "Chinese", "Japanese"]
    },
    {
        "id": 2,
        "name": "Shanghai First People's Hospital",
        "location": "Shanghai, China",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=400",
        "departments": ["Cardiology", "Orthopedics", "TCM", "Dermatology"],
        "languages": ["English", "Chinese", "Korean"]
    },
    {
        "id": 3,
        "name": "Guangdong Provincial People's Hospital",
        "location": "Guangzhou, China",
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400",
        "departments": ["Oncology", "Cardiology", "Reproductive", "Pediatrics"],
        "languages": ["English", "Chinese", "Russian"]
    }
]


@router.get("/")
async def get_hospitals(
    department: Optional[str] = None,
    city: Optional[str] = None,
    search: Optional[str] = None
):
    results = hospitals_data
    if department:
        results = [h for h in results if department in h["departments"]]
    if city:
        results = [h for h in results if city in h["location"]]
    if search:
        results = [h for h in results if search.lower() in h["name"].lower()]
    return results


@router.get("/{hospital_id}")
async def get_hospital(hospital_id: int):
    hospital = next((h for h in hospitals_data if h["id"] == hospital_id), None)
    if hospital:
        return hospital
    return {"error": "Hospital not found"}
