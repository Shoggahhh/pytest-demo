import sys
from typing import Any

import pytest
import httpx


EXPECTED_TYPES: dict[str, type | tuple[type[Any], type[None]]] = {
    "id": int,
    "category": dict,
    "name": str,
    "photoUrls": list,
    "tags": list,
    "status": (str, type(None)),
}


def test_get_pet(client_httpx: httpx.Client) -> None:
    response = client_httpx.get("/pet/1", timeout=5)
    assert response.status_code == 200


def validate_pet_responses(data: dict[Any, Any]) -> None:
    for key, exp_type in EXPECTED_TYPES.items():
        assert key in data, f"Missing field: {key}"
        assert isinstance(data[key], exp_type), f"Field {key} has wrong type"

    assert all(isinstance(i, str) for i in data.get("photoUrls", []))

    for tag in data.get("tags", []):
        assert isinstance(tag, dict)
        assert "id" in tag and isinstance(tag["id"], int)
        assert "name" in tag and (isinstance(tag["name"], str) or tag["name"] is None)

    if data.get("category", {}) is not None:
        assert isinstance(data["category"], dict)
        assert "id" in data["category"] and isinstance(data["category"]["id"], int)
        assert "name" in data["category"] and (isinstance(data["category"]["name"], str) or data["category"]["name"] is None)


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
def test_pet_response(client_httpx: httpx.Client, url_path: str) -> None:
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
    validate_pet_responses(data)

    assert data["id"] >= 0

    if data["status"] is not None:
        assert data["status"] in (
            "available",
            "pending",
            "sold",
            "7000",
            "5000",
            "6000",
            "string",
            "unavailable",
            "jambom",
        )
