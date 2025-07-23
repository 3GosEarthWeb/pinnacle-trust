from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.transaction_schema import TransactionCreate, TransactionOut
from app.models.user_model import User
from app.services.transaction_service import create_transaction, get_user_transactions, get_all_transactions
from app.dependencies.auth_dependencies import get_current_user, get_db
from app.dependencies.rbac_dependencies import require_roles

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionOut)
def create_new_transaction(data: TransactionCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_transaction(db, data, user)


@router.get("/me", response_model=list[TransactionOut])
def get_my_transactions(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_user_transactions(db, user.id)


@router.get("/all", response_model=list[TransactionOut], dependencies=[Depends(require_roles(["admin"]))])
def get_all_user_transactions(db: Session = Depends(get_db)):
    return get_all_transactions(db)
