import pytest
from app import app
from datetime import datetime
import pytz

@pytest.fixture()
def app2():
    app_instance = app
    app_instance.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app_instance

    # clean up / reset resources here


@pytest.fixture()
def client(app2):
    return app2.test_client()


@pytest.fixture()
def runner(app2):
    return app2.test_cli_runner()


def test_time(client):
    """Test corectness of time without seconds."""

    resp = client.get("/")
    time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")

    assert resp.status_code == 200
    assert time in str(resp.data)