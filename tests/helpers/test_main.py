"""System module"""
from datetime import datetime, timezone, timedelta
import pytest
from httpx import AsyncClient
from app_python.main import app

@pytest.mark.anyio
async def test_moscow_time():
    """ test moscow time endpoint"""
    offset = timezone(timedelta(hours=3))
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as async_client:
        response = await async_client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    api_response = response.json().split("T")
    expected_response = str(datetime.now(offset)).split(" ")
    assert api_response[0] == expected_response[0]
    api_response = api_response[1].split(".")
    expected_response = expected_response[1].split(".")
    assert api_response[0] == expected_response[0]
