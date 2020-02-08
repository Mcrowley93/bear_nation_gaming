from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from reviews.models import Review
from blogs.models import Post
from checkout.models import Order, OrderLineItem, Product
from django.core.paginator import Paginator


# Registration View
def register(request):
    """ Render the registration page """
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in! Log out to register a new user!")
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'users/register.html', {"registration_form": registration_form})


# Login View
def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in!")
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

        # Code to allow accounts to login with both username/email was adapted from https://www.youtube.com/watch?v=c7PqMsQiWKU
        try:
            user = auth.authenticate(username=User.objects.get(email=username), password=password)
        except:
            user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(user=user, request=request)
            messages.success(request, "You have successfully logged in!")
            return redirect(reverse('home'))
        else:
            messages.error(request, "Your username or password is incorrect")

    else:
        login_form = UserLoginForm()
    return render(request, 'users/login.html', {'login_form': login_form})


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('home'))


# help with pagination from: https://docs.djangoproject.com/en/2.2/topics/pagination/
@login_required
def user_account(request):
    posts = Post.objects.all()
    reviews = Review.objects.all()
    user_orders = OrderLineItem.objects.all()
    return render(request, 'users/user_account.html', {"reviews": reviews, "posts": posts, "user_orders": user_orders})
