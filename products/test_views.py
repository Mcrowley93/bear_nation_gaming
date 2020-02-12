from django.test import TestCase


class TestProductsView(TestCase):

    def test_products_page(self):
        response = self.client.get('/products/all_products/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
