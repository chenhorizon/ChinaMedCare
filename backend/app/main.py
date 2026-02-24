from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import hospitals, doctors, bookings

app = FastAPI(title="ChinaMedCare API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hospitals.router, prefix="/api/hospitals", tags=["hospitals"])
app.include_router(doctors.router, prefix="/api/doctors", tags=["doctors"])
app.include_router(bookings.router, prefix="/api/bookings", tags=["bookings"])


@app.get("/")
async def root():
    return {"message": "Welcome to ChinaMedCare API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
