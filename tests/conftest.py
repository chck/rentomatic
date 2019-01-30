import pytest


from rentomatic.app import create_app
from rentomatic.settings import TestConfig


@pytest.fixture
def app():
    return create_app(TestConfig)