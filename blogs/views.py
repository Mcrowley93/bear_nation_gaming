from django.shortcuts import render


def all_posts(request):
    return render(request, 'blogs/all_posts.html', {})