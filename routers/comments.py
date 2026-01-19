from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.comments import CommentCreate, CommentResponse
from services import comments_service
from routers.auth import get_current_user
from models.user import User

router = APIRouter(tags=["comments"])


@router.post("/blog/{post_id}/comments", response_model=CommentResponse)
def create_comment(
    post_id: int,
    comment: CommentCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return comments_service.create_comment(
        db=db, comment=comment, post_id=post_id, user_id=current_user.id
    )


@router.get("/blog/{post_id}/comments", response_model=List[CommentResponse])
def read_comments(
    post_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Annotated[Session, Depends(get_db)] = None,
):
    return comments_service.get_comments_by_post(
        db, post_id=post_id, skip=skip, limit=limit
    )
