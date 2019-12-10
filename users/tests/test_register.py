from rest_framework.test import APITestCase
from users.models import CustomUser
from decimal import Decimal
from unittest.mock import patch


_to = "_to"


class RegisterTest(APITestCase):
    def setUp(self):
        self.email = "mazda266@gmail.com"
        self.password = "1"

    def test_register_success(self, *args):
        response = self.client.post(f"/auth/register/", data={
            "email": self.email,
            "password": self.password,
            "password2": self.password,
        })
        self.assertEqual(response.status_code, 204)
        # response_data = response.json()

        user = CustomUser.objects.get(email=self.email)

        self.assertEqual(self.email, user.email)
        self.assertEqual(user.check_password(self.password), True)


