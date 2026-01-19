from sqlalchemy.orm import Session
from services import users_service
from config.security import verify_password

def authenticate_user(db: Session, email: str, password: str):
    user = users_service.get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
