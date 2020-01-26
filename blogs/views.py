from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm


def all_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blogs/all_posts.html", {"posts": posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogs/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})


# posts_search function is case insensitive and gets the 'query' and filters the Posts based on name
def posts_search(request):
    posts = Post.objects.filter(title__icontains=request.GET['query'])
    return render(request, "blogs/all_posts.html", {"posts": posts})
