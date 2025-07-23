from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth_dependencies import get_current_admin
from app.services.audit_service import get_audit_logs
from app.database import get_db

router = APIRouter(prefix="/audit", tags=["Audit Logs"])

@router.get("/")
def fetch_audit_logs(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return get_audit_logs(db)
