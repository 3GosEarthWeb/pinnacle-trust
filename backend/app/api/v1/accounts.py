from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.schemas.account_schema import AccountCreate, AccountUpdate, AccountResponse
from app.services.account_service import (
    create_account, get_account_by_id, get_all_accounts, update_account, close_account
)
from app.database import get_db
from app.dependencies.auth_dependencies import get_current_user
from app.schemas.auth_schema import UserResponse

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
def create_new_account(
    account_data: AccountCreate,
    db: Session = Depends(get_db),
    user: UserResponse = Depends(get_current_user),
):
    """
    Create a new bank account. Allowed for admin and employee roles.
    """
    if user.role not in ["admin", "employee"]:
        raise HTTPException(status_code=403, detail="Unauthorized access")
    return create_account(account_data, db)


@router.get("/", response_model=List[AccountResponse])
def list_all_accounts(
    db: Session = Depends(get_db),
    user: UserResponse = Depends(get_current_user),
):
    """
    List all bank accounts (admin only). Customers will only see their own accounts.
    """
    if user.role == "admin":
        return get_all_accounts(db)
    elif user.role == "customer":
        return get_all_accounts(db, customer_id=user.id)
    else:
        raise HTTPException(status_code=403, detail="Unauthorized access")


@router.get("/{account_id}", response_model=AccountResponse)
def get_account(
    account_id: UUID,
    db: Session = Depends(get_db),
    user: UserResponse = Depends(get_current_user),
):
    """
    Get account details by account ID.
    Admins/employees can access all, customers only their own.
    """
    account = get_account_by_id(account_id, db)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    if user.role != "admin" and account.customer_id != user.id:
        raise HTTPException(status_code=403, detail="Unauthorized to view this account")

    return account


@router.put("/{account_id}", response_model=AccountResponse)
def update_account_details(
    account_id: UUID,
    updates: AccountUpdate,
    db: Session = Depends(get_db),
    user: UserResponse = Depends(get_current_user),
):
    """
    Update account (balance/account_type) — Admin or employee only.
    """
    if user.role not in ["admin", "employee"]:
        raise HTTPException(status_code=403, detail="Unauthorized access")
    return update_account(account_id, updates, db)


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def deactivate_account(
    account_id: UUID,
    db: Session = Depends(get_db),
    user: UserResponse = Depends(get_current_user),
):
    """
    Soft delete (close) an account — Admin only.
    """
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can close accounts")
    close_account(account_id, db)
    return None
