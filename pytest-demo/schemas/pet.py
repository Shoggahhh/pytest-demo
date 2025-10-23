from pydantic import BaseModel
from schemas.tag import Tag
from schemas.category import Category


class PetBase(BaseModel):
    id: int
    category: Category | None = None
    name: str
    photoUrls: list[str]
    tags: list[Tag]
    status: str | None = None


class PetCreate(PetBase):
    """
    Model for create pet
    """


class Pet(PetBase):
    """
    Model for Pet
    """
