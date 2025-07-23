from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Support_ticket model

class Support_ticket(Base):
    __tablename__ = 'support_tickets'
    id = Column(Integer, primary_key=True, index=True)
