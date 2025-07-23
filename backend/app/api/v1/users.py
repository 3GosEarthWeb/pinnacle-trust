from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserOut, UserUpdate
from app.models.user_model import User
from app.services.user_service import get_user_by_id, update_user_info
from app.dependencies.auth_dependencies import get_current_user, get_db
from app.dependencies.rbac_dependencies import require_roles

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserOut)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserOut)
def update_my_profile(update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_user_info(db=db, user=current_user, update_data=update)


@router.get("/{user_id}", response_model=UserOut, dependencies=[Depends(require_roles(["admin"]))])
def get_user_by_admin(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
