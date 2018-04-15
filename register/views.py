from django.shortcuts import render

# Create your views here.


def reg(request):   # views for course
    return render(request, 'register/registration.html', {})


def course(request):   # views for course
    return render(request, 'register/course.html', {})


def login1(request):   # views for course
    return render(request, 'register/log_in.html', {})
