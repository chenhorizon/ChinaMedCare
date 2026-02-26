import logging
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import DBHospital, DBAdmin
from app.core.security import DEFAULT_ADMIN_HASH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pre-generated hash for "admin123" (imported from security.py)
ADMIN_PASSWORD_HASH = DEFAULT_ADMIN_HASH


def init_db():
    """Initialize database with default data"""
    db = SessionLocal()
    try:
        # Check if we already have data
        if db.query(DBHospital).count() == 0:
            # Add default hospitals
            default_hospitals = [
                DBHospital(
                    name="Peking Union Medical College Hospital",
                    location="Beijing, China",
                    rating=4.9,
                    image="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400",
                    departments=["Cardiology", "Neurology", "Oncology", "Orthopedics"],
                    languages=["English", "Chinese", "Japanese"]
                ),
                DBHospital(
                    name="Shanghai First People's Hospital",
                    location="Shanghai, China",
                    rating=4.8,
                    image="https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=400",
                    departments=["Cardiology", "Orthopedics", "TCM", "Dermatology"],
                    languages=["English", "Chinese", "Korean"]
                ),
                DBHospital(
                    name="Guangdong Provincial People's Hospital",
                    location="Guangzhou, China",
                    rating=4.7,
                    image="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400",
                    departments=["Oncology", "Cardiology", "Reproductive", "Pediatrics"],
                    languages=["English", "Chinese", "Russian"]
                )
            ]
            for hospital in default_hospitals:
                db.add(hospital)
            db.commit()
            logger.info("Default hospitals added.")
        else:
            logger.info("Hospitals already exist in database.")

        # Check if admin exists
        admin_count = db.query(DBAdmin).count()
        logger.info(f"Admin users in database: {admin_count}")
        if admin_count == 0:
            # Add default admin (password: admin123)
            admin = DBAdmin(
                username="admin",
                hashed_password=ADMIN_PASSWORD_HASH
            )
            db.add(admin)
            db.commit()
            logger.info("Default admin user added.")
        else:
            logger.info("Admin user already exists in database.")

        logger.info("Database initialization complete.")
    except Exception as e:
        logger.error(f"Error during database initialization: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
