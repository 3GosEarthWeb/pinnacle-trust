from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Address model

class Address(Base):
    __tablename__ = 'addresss'
    id = Column(Integer, primary_key=True, index=True)
