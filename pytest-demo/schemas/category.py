from pydantic import BaseModel

class CategoryBase(BaseModel):
    id: int
    name: str | None = None


class Category(CategoryBase):
    """
    Model for Category
    """