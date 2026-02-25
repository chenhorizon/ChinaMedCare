from typing import List, Optional, Dict
from app.models.hospital import Hospital, HospitalCreate, HospitalUpdate


class MockHospitalDB:
    """Mock database for hospitals (in-memory storage)"""

    def __init__(self):
        # Initial mock data
        self._hospitals: Dict[int, Hospital] = {}
        self._next_id = 1
        self._init_default_data()

    def _init_default_data(self):
        """Initialize with default hospital data"""
        default_hospitals = [
            {
                "name": "Peking Union Medical College Hospital",
                "location": "Beijing, China",
                "rating": 4.9,
                "image": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400",
                "departments": ["Cardiology", "Neurology", "Oncology", "Orthopedics"],
                "languages": ["English", "Chinese", "Japanese"]
            },
            {
                "name": "Shanghai First People's Hospital",
                "location": "Shanghai, China",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=400",
                "departments": ["Cardiology", "Orthopedics", "TCM", "Dermatology"],
                "languages": ["English", "Chinese", "Korean"]
            },
            {
                "name": "Guangdong Provincial People's Hospital",
                "location": "Guangzhou, China",
                "rating": 4.7,
                "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400",
                "departments": ["Oncology", "Cardiology", "Reproductive", "Pediatrics"],
                "languages": ["English", "Chinese", "Russian"]
            }
        ]

        for data in default_hospitals:
            self.create(HospitalCreate(**data))

    def get_all(self, page: int = 1, page_size: int = 10,
                search: Optional[str] = None,
                department: Optional[str] = None,
                city: Optional[str] = None) -> tuple[List[Hospital], int]:
        """Get all hospitals with pagination and filters"""
        results = list(self._hospitals.values())

        # Apply filters
        if search:
            search_lower = search.lower()
            results = [h for h in results if search_lower in h.name.lower()]
        if department:
            results = [h for h in results if department in h.departments]
        if city:
            results = [h for h in results if city in h.location]

        # Calculate pagination
        total = len(results)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_results = results[start:end]

        return paginated_results, total

    def get_by_id(self, hospital_id: int) -> Optional[Hospital]:
        """Get hospital by ID"""
        return self._hospitals.get(hospital_id)

    def create(self, hospital_create: HospitalCreate) -> Hospital:
        """Create a new hospital"""
        hospital = Hospital(
            id=self._next_id,
            **hospital_create.model_dump()
        )
        self._hospitals[self._next_id] = hospital
        self._next_id += 1
        return hospital

    def update(self, hospital_id: int, hospital_update: HospitalUpdate) -> Optional[Hospital]:
        """Update an existing hospital"""
        hospital = self._hospitals.get(hospital_id)
        if not hospital:
            return None

        update_data = hospital_update.model_dump(exclude_unset=True)
        updated_hospital = hospital.model_copy(update=update_data)
        self._hospitals[hospital_id] = updated_hospital
        return updated_hospital

    def delete(self, hospital_id: int) -> bool:
        """Delete a hospital"""
        if hospital_id in self._hospitals:
            del self._hospitals[hospital_id]
            return True
        return False


# Global mock database instance
hospital_db = MockHospitalDB()
