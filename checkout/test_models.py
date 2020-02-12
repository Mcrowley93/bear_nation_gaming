from django.test import TestCase
from checkout.models import Order, OrderLineItem, User, Product


class TestCheckoutModels(TestCase):

    def test_place_order(self):
        Order.username = User(username='TomRiddle')
        order = Order(full_name='Tom Riddle',
                      phone_number='07777888888',
                      country='Wizardland',
                      postcode='H0GWAR7',
                      town_or_city='Wizardtown',
                      street_address1='Hogwarts',
                      street_address2='Castle',
                      county='Wizardcounty',
                      username='TomRiddle')

        self.assertEqual(order.full_name, 'Tom Riddle')
        self.assertEqual(order.phone_number, '07777888888')
        self.assertEqual(order.country, 'Wizardland')
        self.assertEqual(order.postcode, 'H0GWAR7')
        self.assertEqual(order.town_or_city, 'Wizardtown')
        self.assertEqual(order.street_address1, 'Hogwarts')
        self.assertEqual(order.street_address2, 'Castle')
        self.assertEqual(order.county, 'Wizardcounty')
        self.assertEqual(order.username, 'TomRiddle')

    def test_place_order_products(self):
        order_line_item = OrderLineItem()
        self.assertFalse(order_line_item.quantity)
