from django.test import TestCase


class TestReviewsView(TestCase):

    def test_reviews_page(self):
        response = self.client.get('/reviews/all_reviews/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')
