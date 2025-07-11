from django.test import TestCase
from django.urls import reverse
from user_auth.models import User

class LoginTests(TestCase):

    def setUp(self):
        self.email = "test@example.com"
        self.password = "TestPass123!"
        self.user = User.objects.create_user(email=self.email, password=self.password)

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password')

    def test_login_success(self):
        response = self.client.post(reverse('login'), {
            'email': self.email,
            'password': self.password,
        })
        self.assertRedirects(response, '/')

    def test_login_failure_invalid_password(self):
        response = self.client.post(reverse('login'), {
            'email': self.email,
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')
