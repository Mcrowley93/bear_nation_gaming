from django.test import TestCase
from accounts.models import User


class TestViews(TestCase):

    def test_get_home_page_whilst_logged_in(self):
        User.objects.create_user(
            username='mainuser',
            email='mainuser@example.com',
            password='password')
        self.client.login(username='mainuser', password='password')
        page = self.client.get("")
        assert b"Welcome back" in page.content
        assert b"mainuser" in page.content
        self.assertEqual(page.status_code, 200)

    def test_get_home_page_whilst_not_logged_in(self):
        page = self.client.get("")
        assert b"Welcome!" in page.content
        self.assertEqual(page.status_code, 200)

    def test_not_logged_in_content_for_guest_user(self):
        page = self.client.get("")
        assert b"mainuser" not in page.content
        self.assertEqual(page.status_code, 200)
