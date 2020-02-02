from django.apps import apps
from django.test import TestCase
from .apps import ProductsConfig


class TestCheckoutConfig(TestCase):

    def test_checkout_app(self):
        self.assertEqual("products", ProductsConfig.name)
        self.assertEqual("products", apps.get_app_config("products").name)
