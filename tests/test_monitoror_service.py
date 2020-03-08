import os
import pytest
import httpx
from bs4 import BeautifulSoup


@pytest.fixture
def monitoror_url():
    url = os.environ.get("MONITOROR_URL")
    if url is None:
        pytest.exit("you must use the MONITOROR_URL environment variable to specify where to call Monitoror")
    return url


@pytest.fixture
def monitoror(monitoror_url) -> httpx.Client:
    return httpx.Client(base_url=monitoror_url)


def test_monitoror_http_endpoint(monitoror):
    r = monitoror.get('/')
    assert r.status_code == 200

    soup = BeautifulSoup(r.text, features="html.parser")
    assert soup.title.string == "Monitoror"
