from django.shortcuts import render, redirect
from .models import Review
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddReviewForm


def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/reviews.html', {"reviews": reviews})


@login_required()
def add_a_review(request):
    if request.method == "POST":
        form = AddReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()

            messages.success(request, "You have successfully added a review!")
            return redirect('all_reviews')
        else:
            messages.error(request, "Unable to add your review at this time")

    else:
        form = AddReviewForm()
    return render(request, 'reviews/add_a_review.html', {"form": form})


# reviews_search function is case insensitive and gets the 'query' and filters the Products based on game_title
def reviews_search(request):
    reviews = Review.objects.filter(game_title__icontains=request.GET['query'])
    return render(request, "reviews/reviews.html", {"reviews": reviews})
