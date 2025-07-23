from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Notification model

class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True, index=True)
