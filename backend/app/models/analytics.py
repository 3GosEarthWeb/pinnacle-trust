from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Analytics model

class Analytics(Base):
    __tablename__ = 'analyticss'
    id = Column(Integer, primary_key=True, index=True)
