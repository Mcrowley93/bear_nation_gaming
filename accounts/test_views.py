from django.test import TestCase


class TestAccountsView(TestCase):

    def test_register_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
