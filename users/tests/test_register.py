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


        # # self.assertEqual(response_data["transaction_id"], response_assert["transaction_id"])
        # # self.assertEqual(response_data["hash"], response_assert["hash"])
        # # self.assertEqual(response_data["_from"], response_assert["_from"])
        # self.assertEqual(response_data["_to"], response_assert["_to"])
        # self.assertEqual(response_data["currency"], response_assert["currency"])
        # self.assertEqual(Decimal(response_data["amount"]), Decimal(response_assert["amount"]))
        # self.assertEqual(response_data["confirmations"], response_assert["confirmations"])
        # self.assertEqual(response_data["confirmed"], response_assert["confirmed"])
        # self.assertEqual(response_data["status"], response_assert["status"])
