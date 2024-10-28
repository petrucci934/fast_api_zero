from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_zero.app import app

client = TestClient(app)


def test_home():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'Hello World!!'}
