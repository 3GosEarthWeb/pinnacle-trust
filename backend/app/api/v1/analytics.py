from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth_dependencies import get_current_admin
from app.database import get_db
from app.services.analytics_service import (
    get_customer_count,
    get_transaction_summary,
    get_total_revenue,
    get_loan_distribution,
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/customers")
def customer_count(admin=Depends(get_current_admin), db: Session = Depends(get_db)):
    return {"total_customers": get_customer_count(db)}

@router.get("/transactions")
def transaction_summary(admin=Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_transaction_summary(db)

@router.get("/revenue")
def total_revenue(admin=Depends(get_current_admin), db: Session = Depends(get_db)):
    return {"revenue": get_total_revenue(db)}

@router.get("/loans")
def loan_distribution(admin=Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_loan_distribution(db)
