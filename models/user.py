from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from .base import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .post import Post
    from .comment import Comment


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    posts: Mapped[List["Post"]] = relationship(back_populates="owner")
    comments: Mapped[List["Comment"]] = relationship(back_populates="owner")
