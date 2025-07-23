from sqlalchemy import Column, Integer, String
from app.models.base import Base

# Loan_repayment model

class Loan_repayment(Base):
    __tablename__ = 'loan_repayments'
    id = Column(Integer, primary_key=True, index=True)
