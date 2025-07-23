from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Audit_log model

class Audit_log(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True, index=True)
