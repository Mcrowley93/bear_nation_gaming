from django.test import TestCase
from django.contrib.auth.models import User


class TestCheckoutView(TestCase):

    # The user must login first before they can reach the checkout
    def setUp(self):
        User.objects.create_user(username='mainuser', email='mainuser@example.com', password='password')
        self.client.login(username='mainuser', password='password')

    def test_checkout_page(self):
        response = self.client.get('/checkout/checkout/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('checkout/checkout.html')
