from django.shortcuts import render

# Create your views here.


def alogin(request):   # views for course
    return render(request, 'other/alogin.html', {})


def mycourses(request):   # views for course
    return render(request, 'other/mycourse.html', {})


def all_courses(request):   # views for course
    return render(request, 'other/all_courses.html', {})


def course_details1(request):   # views for course
    return render(request, 'other/course_details1.html', {})

def course_content1(request):   # views for course
    return render(request, 'other/course_content1.html', {})

