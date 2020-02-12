from django.test import TestCase


class TestCartView(TestCase):

    def test_view_cart_page(self):
        response = self.client.get('/cart/view_cart/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
