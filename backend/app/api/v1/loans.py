from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.loan_schema import LoanCreate, LoanOut, LoanUpdate
from app.models import models
from app.database import get_db
from app.dependencies.auth_dependencies import get_current_user, get_current_admin
from typing import List

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("/", response_model=LoanOut)
def apply_for_loan(loan: LoanCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_loan = models.Loan(**loan.dict(), user_id=user.id, status="Pending")
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan

@router.get("/", response_model=List[LoanOut])
def get_all_loans(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(models.Loan).all()

@router.get("/my", response_model=List[LoanOut])
def get_user_loans(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Loan).filter(models.Loan.user_id == user.id).all()

@router.put("/{loan_id}", response_model=LoanOut)
def update_loan_status(loan_id: int, loan_update: LoanUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    for key, value in loan_update.dict().items():
        setattr(loan, key, value)
    db.commit()
    db.refresh(loan)
    return loan
