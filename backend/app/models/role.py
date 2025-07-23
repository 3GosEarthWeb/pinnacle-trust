from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Role model

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
