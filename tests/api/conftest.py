import pytest
import requests

import truststore
truststore.inject_into_ssl()

BASE_URL = "https://automationintesting.online"


@pytest.fixture
def api():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture
def base_url():
    return BASE_URL