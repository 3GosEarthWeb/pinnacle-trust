from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Loan model

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, index=True)
