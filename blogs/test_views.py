from django.test import TestCase
from blogs.models import Post
from accounts.models import User


class TestViews(TestCase):

    def test_get_community_page_whilst_logged_in(self):
        User.objects.create_user(username='mainuser', email='mainuser@example.com', password='password')
        self.client.login(username='mainuser', password='password')
        page = self.client.get("/blogs/all_posts/")
        assert b"Add New Post" in page.content
        assert b"Community" in page.content
        self.assertEqual(page.status_code, 200)

    def test_get_community_page_whilst_logged_out(self):
        page = self.client.get("/blogs/all_posts/")
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/accounts/login/?next=/blogs/all_posts/')


class TestUserViews(TestCase):

    def setUp(self):
        User.objects.create_user(username='mainuser', email='mainuser@example.com', password='password')
        self.client.login(username='mainuser', password='password')

    def test_get_new_post_page(self):
        page = self.client.get("/blogs/post/new/")
        assert b"New Community Post" in page.content
        assert b"<form method=" in page.content
        self.assertEqual(page.status_code, 200)
