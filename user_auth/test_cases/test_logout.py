from django.test import TestCase
from django.urls import reverse
from user_auth.models import User

class LogoutTests(TestCase):

    def setUp(self):
        self.email = "test@example.com"
        self.password = "TestPass123!"
        self.user = User.objects.create_user(email=self.email, password=self.password)

    def test_logout_redirects(self):
        self.client.login(email=self.email, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

    def test_logout_when_not_logged_in(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
