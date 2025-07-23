from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.auth_dependencies import get_current_user
from app.database import get_db
from app.services.dashboard_service import get_user_dashboard

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def fetch_dashboard(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return get_user_dashboard(user, db)
