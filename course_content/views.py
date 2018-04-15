from django.shortcuts import render, get_object_or_404
from .models import CourseContent

# Create your views here.


def course_content(request, pk):
    course_content = get_object_or_404(CourseContent, pk=pk)
    return render(request, 'course_content/course_content.html', {'course_content': course_content})