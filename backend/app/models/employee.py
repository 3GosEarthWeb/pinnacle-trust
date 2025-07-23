from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Employee model

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
