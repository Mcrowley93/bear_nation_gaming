from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def error_404_view(request, exception):
    return render(request, 'home/error_404.html')
