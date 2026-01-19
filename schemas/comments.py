from pydantic import BaseModel, ConfigDict

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    post_id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
