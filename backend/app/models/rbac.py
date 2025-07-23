from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Rbac model

class Rbac(Base):
    __tablename__ = 'rbacs'
    id = Column(Integer, primary_key=True, index=True)
