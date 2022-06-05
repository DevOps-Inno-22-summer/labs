import pytest
from fastapi.testclient import TestClient

from app import config
from app import factory


@pytest.fixture(scope="session")
def settings():
    return config.Settings()


@pytest.fixture
def app(settings,):
    api_app = factory.build_app(settings)
    return api_app


@pytest.fixture
def client(app):
    return TestClient(app)
