from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.support_schema import SupportTicketCreate, SupportTicketOut
from app.services.support_service import create_ticket, get_user_tickets
from app.dependencies.auth_dependencies import get_current_user, get_db
from app.models.user_model import User

router = APIRouter(prefix="/support", tags=["Support"])


@router.post("/", response_model=SupportTicketOut, status_code=status.HTTP_201_CREATED)
def submit_ticket(data: SupportTicketCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_ticket(db, data, user)


@router.get("/me", response_model=list[SupportTicketOut])
def list_my_tickets(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_user_tickets(db, user.id)
