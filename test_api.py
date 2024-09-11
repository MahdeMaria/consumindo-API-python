import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200

def test_get_item(client):
    response = client.get('/items/1')
    assert response.status_code == 200

def test_create_item(client):
    response = client.post('/items', json={'title': 'Novo Item', 'body': 'Descrição do item'})
    assert response.status_code == 201

def test_update_item(client):
    response = client.put('/items/1', json={'title': 'Item Atualizado', 'body': 'Descrição atualizada'})
    assert response.status_code == 200

def test_delete_item(client):
    response = client.delete('/items/1')
    assert response.status_code == 204
