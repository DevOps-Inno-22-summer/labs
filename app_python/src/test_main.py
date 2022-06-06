from datetime import datetime
from fastapi.testclient import TestClient
from pytz import timezone

from main import app, getMoscowTime

client = TestClient(app)


def test_getMoscowTime():
    assert getMoscowTime() == datetime.now(
        timezone('Europe/Moscow')).strftime('%Y-%m-%d_%H:%M:%S')


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Moscow time": getMoscowTime()}
