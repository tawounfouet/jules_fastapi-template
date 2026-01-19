from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Integer
from .base import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .comment import Comment

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    content: Mapped[str] = mapped_column(Text)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    owner: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")
