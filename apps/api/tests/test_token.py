from django.test import TestCase
from django.contrib.auth.models import User


class TokenTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('my_strong_pass')
        self.user.save()
        self.url = '/api/v1/token/'

    def test_login(self):
        credentials = {
            'username': 'testuser',
            'password': 'my_strong_pass'
        }
        response = self.client.post(self.url, data=credentials)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_fail(self):
        credentials = {
            'username': 'testuser',
            'password': 'my_wrong_pass'
        }
        response = self.client.post(self.url, data=credentials)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 401)

    def tearDown(self):
        self.user.delete()
