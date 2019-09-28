from .models import UserModel
from .models import FavoriteModel
from .models import ClientModel

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class FavoritesListTestCase(APITestCase):
    """=========================================================================
    Classe de testes da API.
    ========================================================================="""

    fixtures = [
        'user.json',
        'client.json'
        ]

    def setUp(self):
        """=====================================================================
        Instancia APIClient e loga utilizando superuser.
        ====================================================================="""
        self.client = APIClient()
        self.token = UserModel.objects.get(email="teste@teste.com").token

    def test_get_api_root(self):
        """=====================================================================
        Testa método get em APIRoot.
        ====================================================================="""
        response = self.client.get('http://localhost:8000/api/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_user(self):
        """=====================================================================
        Testa método post em "/api/user/".
        ====================================================================="""
        response = self.client.post('http://localhost:8000/api/user/',
                                {
                                "username": "testee",
                                "first_name": "testee",
                                "last_name": "testee",
                                "email": "teste@testee.com"
                                })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_client(self):
        """=====================================================================
        Testa Método get em "/api/<TOKEN>/client/".
        ====================================================================="""
        response = self.client.get(f'http://localhost:8000/api/{self.token}/client/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_client(self):
        """=====================================================================
        Testa Método post em "/api/<TOKEN>/client/".
        ====================================================================="""
        response = self.client.post(f'http://localhost:8000/api/{self.token}/client/',
                                    {
                                    "name": "Teste Testee",
                                    "email": "teste@testee.com"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch_client(self):
        """=====================================================================
        Testa Método patch em "/api/<TOKEN>/client/<EMAIL-DO-CLIENTE>".
        ====================================================================="""
        response = self.client.patch(f'http://localhost:8000/api/{self.token}/client/teste@teste.com/',
                                    {
                                    "name": "testado",
                                    "email": "testado@testado.com"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_client(self):
        """=====================================================================
        Testa Método delete em "/api/<TOKEN>/client/<EMAIL-DO-CLIENTE>".
        ====================================================================="""
        response = self.client.delete(f'http://localhost:8000/api/{self.token}/client/teste@teste.com/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_favorites(self):
        """=====================================================================
        Testa Método get em "/api/<TOKEN>/client/<EMAIL-DO-CLIENTE>/list".
        ====================================================================="""
        response = self.client.get(f'http://localhost:8000/api/{self.token}/client/teste@teste.com/list/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_favorites(self):
        """=====================================================================
        Testa método post em "/api/<TOKEN>/client/<EMAIL-DO-CLIENTE>/list".
        ====================================================================="""
        response = self.client.post(f'http://localhost:8000/api/{self.token}/client/teste@teste.com/list/',
                                {
                                "id": "356eafd9-224a-d242-a3f2-e29b4270a927"
                                })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
