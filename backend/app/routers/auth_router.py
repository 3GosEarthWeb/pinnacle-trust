from fastapi import APIRouter, Depends
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.services.auth_service import register_user, login_user

router = APIRouter()

@router.post("/register")
def register(payload: RegisterRequest):
    return register_user(payload)

@router.post("/login")
def login(payload: LoginRequest):
    return login_user(payload)
