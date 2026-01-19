from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey, Integer
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .post import Post


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"))

    owner: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments")
