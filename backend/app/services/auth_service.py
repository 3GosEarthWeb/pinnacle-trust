from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth_schema import RegisterRequest
from app.utils.token_utils import create_access_token
from uuid import uuid4
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def register_user(db: Session, request: RegisterRequest):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        id=uuid4(),
        full_name=request.full_name,
        email=request.email,
        phone=request.phone,
        password_hash=hash_password(request.password),
        role="customer",
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

