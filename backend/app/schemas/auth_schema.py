from pydantic import BaseModel, EmailStr, constr
from typing import Optional, Annotated
from uuid import UUID
from datetime import datetime

# Type-safe annotated strings
FullNameStr = Annotated[str, constr(min_length=3, max_length=100)]
PasswordStr = Annotated[str, constr(min_length=8)]

# -------------------------------
# Auth Request Schemas
# -------------------------------

class RegisterRequest(BaseModel):
    full_name: FullNameStr
    email: EmailStr
    password: PasswordStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# -------------------------------
# Auth Response Schemas
# -------------------------------

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class TokenData(BaseModel):
    sub: Optional[str] = None  # subject (usually user id or email)
    exp: Optional[int] = None  # expiration


class UserResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
