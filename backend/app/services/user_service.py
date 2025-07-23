from sqlalchemy.orm import Session
from uuid import UUID
from typing import Optional, List
from app.schemas.auth_schema import RegisterRequest
from app.models.user import User


def get_user_by_id(db: Session, user_id: UUID) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_data: RegisterRequest, hashed_password: str) -> User:
    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password=hashed_password,
        phone=user_data.phone,
        role="customer",  # Default role; can be parameterized
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()


def delete_user(db: Session, user_id: UUID) -> bool:
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
