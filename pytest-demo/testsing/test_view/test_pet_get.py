import pytest
import httpx
from pydantic import ValidationError
from schemas.pet import Pet


def test_get_pet(client_httpx: httpx.Client) -> None:
    response = client_httpx.get("/pet/1", timeout=5)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_path",
    [
        "/pet/1",
        "/pet/2",
        "/pet/3",
        "/pet/4",
        "/pet/5",
    ],
)
def test_get_pet_response(client_httpx: httpx.Client, url_path: str) -> None:
    response = client_httpx.get(
        url_path,
        timeout=5,
    )
    assert response.status_code in (
        200,
        404,
    ), f"Unexpected status code: {response.status_code}"
    if response.status_code == 404:
        data = response.json()
        assert isinstance(data, dict)
        assert "message" in data
        return

    data = response.json()
    assert isinstance(data, dict)
    try:
        Pet.model_validate(data)
    except ValidationError as ex:
        pytest.fail(f"Pydantic validation error {ex.errors()[0]['msg']}")
