from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.blog import PostCreate, PostResponse
from services import blog_service
from routers.auth import get_current_user
from models.user import User

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/", response_model=PostResponse)
def create_post(
    post: PostCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return blog_service.create_post(db=db, post=post, user_id=current_user.id)


@router.get("/", response_model=List[PostResponse])
def read_posts(
    skip: int = 0, limit: int = 100, db: Annotated[Session, Depends(get_db)] = None
):
    return blog_service.get_posts(db, skip=skip, limit=limit)
