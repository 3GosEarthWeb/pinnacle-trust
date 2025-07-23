from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Account model

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
