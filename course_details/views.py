from django.shortcuts import render, get_object_or_404

from .models import CourseDetails


# Create your views here.

def course_details(request, pk):
    course_details = get_object_or_404(CourseDetails, pk=pk)
    return render(request, 'course_details/course_details.html', {'course_content': course_details})

