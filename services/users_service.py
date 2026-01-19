from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from schemas.users import UserCreate
from config.security import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.execute(select(User).where(User.email == email)).scalar_one_or_none()

def get_user_by_id(db: Session, user_id: int):
    return db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.execute(select(User).offset(skip).limit(limit)).scalars().all()

def create_user(db: Session, user: UserCreate):
    # Check if user exists
    if get_user_by_email(db, user.email):
        return None

    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
