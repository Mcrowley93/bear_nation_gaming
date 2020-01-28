from django.db import models
from accounts.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Productreview(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='productreviews')
    reviewer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.review
