from collections.abc import Generator
import httpx
import pytest

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture
def client_httpx() -> Generator[httpx.Client]:
    with httpx.Client(base_url=BASE_URL) as client:
        yield client
