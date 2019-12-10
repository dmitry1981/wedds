from rest_framework.test import APITestCase
from users.models import CustomUser


class RegisterTest(APITestCase):
    def setUp(self):
        self.email = "mazda266@gmail.com"
        self.password = "1"
        self.activation_code = "1"
        user = CustomUser.objects.create_user(email=self.email)
        user.activation_code = self.activation_code
        user.is_active = False
        user.save()

    def test_activate_success(self, *args):
        response = self.client.get(f"/auth/activate/?code={self.activation_code}")
        self.assertEqual(response.status_code, 204)
        # response_data = response.json()

        user = CustomUser.objects.get(email=self.email)
        self.assertEqual(user.is_active, True)

