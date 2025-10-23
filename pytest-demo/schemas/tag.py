from pydantic import BaseModel


class TagBase(BaseModel):
    id: int
    name: str | None = None


class Tag(TagBase):
    """
    Model for Tag
    """
