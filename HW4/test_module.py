import requests
import pytest


def test_url_status_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code)