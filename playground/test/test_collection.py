import pytest
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_400(client):
        # AAA(Arrange, Act, Assert)

        # A - Arrange

        # A - Act
        client = APIClient()
        response = client.post("/store/collections/", data={"title": "a"})

        # A - Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
