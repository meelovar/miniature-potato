import pytest

from main import create_app


@pytest.fixture
def client(event_loop, aiohttp_client):
    app = create_app()

    return event_loop.run_until_complete(aiohttp_client(app))


async def test_healthcheck(client):
    response = await client.get("/healthcheck")

    assert response.status == 200
    assert await response.json() == {}


async def test_hash_correct_data(client):
    response = await client.post("/hash", json={"string": "string"})

    assert response.status == 200
    assert (await response.json())["hash_string"] == "473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8"


async def test_hash_incorrect_data(client):
    response = await client.post("/hash", json={"test": "string"})

    assert response.status == 400
    assert await response.json() == {"validation_errors": "Missing required field: 'string'"}
