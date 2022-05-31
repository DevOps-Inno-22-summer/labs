"""Tests for web application."""
from datetime import datetime
import pytest
import pytz
from main import app


@pytest.fixture
def client():
    """Fixture for application."""
    with app.test_client() as client:
        yield client


def test_time(client):
    """Test corectness of time without seconds."""
    resp = client.get("/")
    time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M")
    html_string = 'Current Moscow time (UTC+03:00): {}'.format(time)
    assert resp.status_code == 200
    assert html_string in str(resp.data)
