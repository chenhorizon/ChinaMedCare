from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
from app.api import hospitals, doctors, bookings
from app.api.admin import auth as admin_auth
from app.api.admin import hospitals as admin_hospitals
from app.db import engine, Base
from app.db.init_db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ChinaMedCare API", version="1.0.0")

# Get allowed origins from environment variable
# Format: "https://domain1.com,https://domain2.com"
cors_origins_env = os.getenv("CORS_ORIGINS", "")
allowed_origins = []

if cors_origins_env:
    # Split by comma and trim whitespace
    allowed_origins = [origin.strip() for origin in cors_origins_env.split(",") if origin.strip()]
    logger.info(f"Allowed CORS origins: {allowed_origins}")
else:
    # Default to localhost for development
    allowed_origins = [
        "http://localhost:3000",
        "http://localhost",
        "http://localhost:5173",
    ]
    logger.info(f"No CORS_ORIGINS set, using defaults: {allowed_origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    logger.info(f"Headers: {dict(request.headers)}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Public API routes
app.include_router(hospitals.router, prefix="/api/hospitals", tags=["hospitals"])
app.include_router(doctors.router, prefix="/api/doctors", tags=["doctors"])
app.include_router(bookings.router, prefix="/api/bookings", tags=["bookings"])

# Admin API routes
app.include_router(admin_auth.router, prefix="/api/admin", tags=["admin-auth"])
app.include_router(admin_hospitals.router, prefix="/api/admin/hospitals", tags=["admin-hospitals"])


@app.on_event("startup")
def on_startup():
    """Initialize database on startup"""
    # Create tables
    Base.metadata.create_all(bind=engine)
    # Initialize with default data
    init_db()


@app.get("/")
async def root():
    return {"message": "Welcome to ChinaMedCare API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
