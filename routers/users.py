from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.users import UserCreate, UserResponse
from services import users_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    db_user = users_service.create_user(db=db, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_user


@router.get("/", response_model=List[UserResponse])
def read_users(
    skip: int = 0, limit: int = 100, db: Annotated[Session, Depends(get_db)] = None
):
    users = users_service.get_users(db, skip=skip, limit=limit)
    return users
