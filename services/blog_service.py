from sqlalchemy.orm import Session
from sqlalchemy import select
from models.post import Post
from schemas.blog import PostCreate

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.execute(select(Post).offset(skip).limit(limit)).scalars().all()

def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.model_dump(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
