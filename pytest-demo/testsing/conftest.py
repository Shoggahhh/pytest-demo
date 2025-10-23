from collections.abc import Generator
import httpx
import pytest

from schemas.category import Category
from schemas.pet import PetCreate
from schemas.tag import Tag

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture
def client_httpx() -> Generator[httpx.Client]:
    with httpx.Client(base_url=BASE_URL) as client:
        yield client


def build_pet(
    id_pet: int = 100,
    category: Category = Category(id=0, name="best_dogs",),
    name: str = "my_dog",
    status: str = "available",
    tags: Tag = Tag(id=0, name="best_dogs",)
) -> PetCreate:
    return PetCreate(
        id=id_pet,
        category=category,
        name=name,
        photoUrls=["https://some_url_to_photo.com"],
        tags=[tags],
        status=status,
    )