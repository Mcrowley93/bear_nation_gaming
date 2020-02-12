from django.test import TestCase
from accounts.models import User


class TestUserModel(TestCase):

    def test_create_user(self):
        user = User(username='Max',
                    email='max@gmail.com',
                    password='minimumpassword')

        self.assertEqual(user.username, 'Max')
        self.assertEqual(user.email, 'max@gmail.com')
        self.assertEqual(user.password, 'minimumpassword')


