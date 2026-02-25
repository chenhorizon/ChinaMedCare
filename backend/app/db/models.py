from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.ext.mutable import MutableList
from app.db.database import Base


class DBHospital(Base):
    """Hospital database model"""
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    location = Column(String(200), nullable=False, index=True)
    rating = Column(Float, nullable=False)
    image = Column(String, nullable=False)
    departments = Column(MutableList.as_mutable(JSON), default=list)
    languages = Column(MutableList.as_mutable(JSON), default=list)


class DBAdmin(Base):
    """Admin user database model"""
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
