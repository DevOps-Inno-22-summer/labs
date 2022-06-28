"""System module"""
from datetime import datetime, timezone, timedelta
import pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.anyio
async def test_moscow_time():
    """ test moscow time endpoint"""
    # Arrange
    # Act
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as async_client:
        response = await async_client.get("/")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    api_response = response.json().split("T")
    offset = timezone(timedelta(hours=3))
    expected_response = str(datetime.now(offset)).split(" ")
    assert api_response[0] == expected_response[0]
    api_response = api_response[1].split(".")
    expected_response = expected_response[1].split(".")
    assert api_response[0] == expected_response[0]

@pytest.mark.anyio
async def test_visits_endpoint():
    """ Test visits endpoint"""
    # Arrange
    # Act
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as async_client:
        response = await async_client.get("/visits")
    # Assert
    assert response.status_code == 200
