from fastapi.testclient import TestClient
from fastapi import status
from routes.student import student

client = TestClient(student=student)

def test_index_returns_correct():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK