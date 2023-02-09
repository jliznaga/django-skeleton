from django.test import TestCase
from django.contrib.auth.models import User


class AuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('my_strong_pass')
        self.user.save()

    def test_login(self):
        logged_in = self.client.login(
            username='testuser', password='my_strong_pass')
        self.assertTrue(logged_in)

    def test_login_fail(self):
        logged_in = self.client.login(
            username='testuser', password='my_wrong_pass')
        self.assertFalse(logged_in)

    def tearDown(self):
        self.user.delete()
