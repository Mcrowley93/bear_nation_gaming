from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddReviewForm
from django.core.paginator import Paginator


def all_reviews(request):
    reviews = Review.objects.all()
    paginator = Paginator(reviews, 6)
    page = request.GET.get('page')
    paged_reviews = paginator.get_page(page)
    return render(request, 'reviews/reviews.html', {"reviews": paged_reviews})


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


@login_required()
def edit_a_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user != review.author:
        messages.error(request, "You can only edit the reviews you have written!")
        return redirect('all_reviews')
    if request.method == "POST":
        form = AddReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()

            messages.success(request, "You have successfully edited your review!")
            return redirect('read_review', pk=review.pk)
    else:
        form = AddReviewForm(instance=review)
    return render(request, 'reviews/edit_a_review.html', {'form': form})


# reviews_search function is case insensitive and gets the 'query' and filters the Products based on game_title
def reviews_search(request):
    reviews = Review.objects.filter(game_title__icontains=request.GET['query']) | Review.objects.filter(platform__icontains=request.GET['query']) | Review.objects.filter(score__icontains=request.GET['query'])
    return render(request, "reviews/reviews.html", {"reviews": reviews})


def read_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/read_review.html', {'review': review})


@login_required()
def remove_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user != review.author:
        messages.error(request, "You can only delete the reviews you have submitted!")
        return redirect('all_reviews')
    review.delete()
    return redirect('all_reviews')
