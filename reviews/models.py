from django.db import models
from accounts.models import User


class Review(models.Model):
	game_title = models.CharField(max_length=254, default='')
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	review = models.TextField()
	score = models.IntegerField()
	image = models.ImageField(upload_to='images')
