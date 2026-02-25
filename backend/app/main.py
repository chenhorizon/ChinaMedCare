from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.api import hospitals, doctors, bookings

app = FastAPI(title="ChinaMedCare API", version="1.0.0")

# Get allowed origins from environment variable or use defaults
allowed_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
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
