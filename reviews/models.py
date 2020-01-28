from django.db import models
from accounts.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
	game_title = models.CharField(max_length=254, default='')
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	created_date = models.DateTimeField(default=timezone.now)
	platform = models.CharField(max_length=254, default='')
	review = models.TextField()
	score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
