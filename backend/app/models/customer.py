from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Customer model

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True)
