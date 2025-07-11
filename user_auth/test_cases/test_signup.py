from django.test import TestCase
from django.urls import reverse
from user_auth.models import User

class SignupTests(TestCase):

    def test_signup_page_loads(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Confirm Password')

    def test_signup_success(self):
        response = self.client.post(reverse('signup'), {
            'email': 'newuser@example.com',
            'password': 'NewPass123!',
            'confirm_password': 'NewPass123!',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())

    def test_signup_password_mismatch(self):
        response = self.client.post(reverse('signup'), {
            'email': 'newuser2@example.com',
            'password': 'pass1',
            'confirm_password': 'pass2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Passwords do not match")
