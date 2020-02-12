from django.test import TestCase
from reviews.models import Review, User


class TestReviewModel(TestCase):

    def test_create_review(self):
        Review.author = User(username='Teddy')
        review = Review(game_title='Breath Of The Wild',
                        author='Teddy',
                        platform='Switch',
                        review='Absolutely breath-taking game!',
                        score='9')

        self.assertEqual(review.game_title, 'Breath Of The Wild')
        self.assertEqual(review.author, 'Teddy')
        self.assertEqual(review.platform, 'Switch')
        self.assertEqual(review.review, 'Absolutely breath-taking game!')
        self.assertEqual(review.score, '9')
