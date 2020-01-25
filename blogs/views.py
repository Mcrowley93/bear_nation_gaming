from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def all_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blogs/all_posts.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})


# posts_search function is case insensitive and gets the 'query' and filters the Posts based on name
def posts_search(request):
    posts = Post.objects.filter(title__icontains=request.GET['query'])
    return render(request, "blogs/all_posts.html", {"posts": posts})
