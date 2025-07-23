from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse, UserResponse
from app.services.auth_service import register_user, authenticate_user
from app.dependencies.auth_dependencies import get_current_user
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user_route(payload: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, payload)
    return user


@router.post("/login", response_model=TokenResponse)
def login_route(payload: LoginRequest, db: Session = Depends(get_db)):
    token = authenticate_user(db, payload)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return token


@router.get("/me", response_model=UserResponse)
def get_current_user_route(current_user=Depends(get_current_user)):
    return current_user


# Optional: Example of protected route for role-based access
@router.get("/admin-only", response_model=dict)
def admin_only_route(current_user=Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return {"message": "Welcome Admin!"}
