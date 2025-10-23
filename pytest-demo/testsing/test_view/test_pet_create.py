import httpx
import pytest
from _pytest.fixtures import SubRequest

from testsing.conftest import build_pet
from typing import Any
import json


class TestCreatePet:
    @pytest.fixture(
        params=[
            pytest.param(("abc", "name-too-short"), id="name-too-short"),
            pytest.param(("abc" * 100, "name-too-long"), id="name-too-long"),
        ]
    )
    def create_pet_values(self, request: SubRequest) -> dict[str, Any]:
        build = build_pet()
        data: dict[str, Any] = build.model_dump(mode="json")
        name, err = request.param
        data["name"] = name
        return data

    def test_create_pet(
        self, client_httpx: httpx.Client, create_pet_values: dict[str, Any]
    ) -> None:
        response = client_httpx.post("/pet", json=create_pet_values)

        assert (response.status_code == 200), response.text

    def test_create_pet_fail(self, client_httpx: httpx.Client) -> None:
        build = build_pet()
        data: dict[str, Any] = build.model_dump(mode="json")
        fail_json = json.dumps(data)
        fail_json = fail_json[:-1]

        response = client_httpx.post("/pet", content=fail_json)

        assert response.status_code == 415, response.text



