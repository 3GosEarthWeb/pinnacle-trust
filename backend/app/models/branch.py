from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Branch model

class Branch(Base):
    __tablename__ = 'branchs'
    id = Column(Integer, primary_key=True, index=True)
