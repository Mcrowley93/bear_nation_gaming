from django.shortcuts import render

def home(request):
    welcome = "Hello World!"
    return render (request, 'products/home.html', {'message': welcome})
