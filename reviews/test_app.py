from django.apps import apps
from django.test import TestCase
from .apps import ReviewsConfig


class TestAccountsConfig(TestCase):

    def test_accounts_app(self):
        self.assertEqual("reviews", ReviewsConfig.name)
        self.assertEqual("reviews", apps.get_app_config("reviews").name)
