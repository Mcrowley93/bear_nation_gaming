from django import forms
from products.models import Productreview


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = Productreview
        fields = ('review', 'rating',)
