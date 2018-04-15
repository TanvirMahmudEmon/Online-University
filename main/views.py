from django.shortcuts import render  # For Home Page


def home(request):   # views for homepage
    return render(request, 'main/base2.html', {})
