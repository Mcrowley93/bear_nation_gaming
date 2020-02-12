from django.test import TestCase
from products.models import Product


class TestProductsModel(TestCase):

    def test_create_product(self):
        product = Product(name='Playstation Controller',
                          description='This is what we use to play video games',
                          image='ps4_controller.jpg',
                          price='39.99')

        self.assertEqual(product.name, 'Playstation Controller')
        self.assertEqual(product.description, 'This is what we use to play video games')
        self.assertEqual(product.image, 'ps4_controller.jpg')
        self.assertEqual(product.price, '39.99')
