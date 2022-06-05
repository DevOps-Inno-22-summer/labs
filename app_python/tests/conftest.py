import pytest
from fastapi.testclient import TestClient


from app import factory
from app import config


@pytest.fixture(scope="session")
def settings():
    return config.Settings()


@pytest.fixture
def app(settings):
    api_app = factory.build_app(settings)
    return api_app


@pytest.fixture
def client(app):
    return TestClient(app)
