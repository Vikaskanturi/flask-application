import pytest
from app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_text = 'GFG43'
    assert expected_text.encode() in response.data


def test_hash(client):
    text = 'test'
    response = client.get(f'/hash/{text}')
    assert response.status_code == 200
    # SHA-256 hash of 'test'
    import hashlib
    expected_hash = hashlib.sha256(text.encode()).hexdigest()
    assert response.data.decode() == expected_hash
