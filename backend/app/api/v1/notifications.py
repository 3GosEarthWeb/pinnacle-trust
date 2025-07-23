from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.notifications_schema import NotificationCreate, NotificationOut
from app.models import models
from app.database import get_db
from app.dependencies.auth_dependencies import get_current_admin
from typing import List

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/", response_model=NotificationOut, status_code=status.HTTP_201_CREATED)
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    db_notification = models.Notification(**notification.dict(), created_by=admin.id)
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.get("/", response_model=List[NotificationOut])
def list_notifications(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(models.Notification).all()

@router.get("/user/{user_id}", response_model=List[NotificationOut])
def user_notifications(user_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()
