import pytest
from myorg.myapi.app import myapi


@pytest.fixture
def app():
    return myapi
