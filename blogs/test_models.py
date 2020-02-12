from django.test import TestCase
from blogs.models import Post, Comment, User


class TestPostModel(TestCase):

    def test_create_post(self):
        Post.author = User(username='Max')
        post = Post(author='Max', title='My first test post', text='This is my first test post')
        self.assertEqual(post.author, 'Max')
        self.assertEqual(post.title, 'My first test post')
        self.assertEqual(post.text, 'This is my first test post')


class TestCommentModel(TestCase):

    def test_create_comment(self):
        Comment.post = Post(title='Post being commented on')
        Comment.author = User(username='James')
        comment = Comment(author='James',
                          text='This is my first test comment')

        self.assertEqual(comment.author, 'James')
        self.assertEqual(comment.text, 'This is my first test comment')
