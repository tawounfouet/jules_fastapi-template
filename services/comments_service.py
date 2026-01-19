from sqlalchemy.orm import Session
from sqlalchemy import select
from models.comment import Comment
from schemas.comments import CommentCreate

def get_comments_by_post(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.execute(
        select(Comment).where(Comment.post_id == post_id).offset(skip).limit(limit)
    ).scalars().all()

def create_comment(db: Session, comment: CommentCreate, post_id: int, user_id: int):
    db_comment = Comment(**comment.model_dump(), post_id=post_id, owner_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
