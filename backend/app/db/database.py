from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get database URL from environment or use SQLite as fallback
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chinamedcare.db")

# For SQLite, we need to add check_same_thread=False
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# Try to create engine with original DATABASE_URL, fall back to SQLite if it fails
try:
    engine = create_engine(
        DATABASE_URL,
        connect_args=connect_args,
        pool_pre_ping=True,
        pool_recycle=300,
    )
    # Test the connection
    if not DATABASE_URL.startswith("sqlite"):
        try:
            with engine.connect():
                logger.info(f"Successfully connected to database: {DATABASE_URL.split('@')[-1] if '@' in DATABASE_URL else DATABASE_URL}")
        except Exception as e:
            logger.warning(f"Failed to connect to database: {e}")
            logger.info("Falling back to SQLite database")
            DATABASE_URL = "sqlite:///./chinamedcare.db"
            connect_args = {"check_same_thread": False}
            engine = create_engine(
                DATABASE_URL,
                connect_args=connect_args
            )
except Exception as e:
    logger.error(f"Error creating engine: {e}")
    logger.info("Falling back to SQLite database")
    DATABASE_URL = "sqlite:///./chinamedcare.db"
    connect_args = {"check_same_thread": False}
    engine = create_engine(
        DATABASE_URL,
        connect_args=connect_args
    )

# Create session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
