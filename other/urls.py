from django.conf.urls import include, url

from other.views import alogin,mycourses,all_courses,course_details1,course_content1


urlpatterns = [
    url(r'^alogin/$', alogin, name='alogin'),  # http://127.0.0.1:8000/other/alogin/
    url(r'^mycourses/$', mycourses, name='mycourses'),  # http://127.0.0.1:8000/other/mycourses/
    url(r'^all_courses/$', all_courses, name='all_courses'),  # http://127.0.0.1:8000/other/all_courses/
    url(r'^course_details1/$', course_details1, name='course_details1'),  # http://127.0.0.1:8000/other/course_details1/
    url(r'^course_content1/$', course_content1, name='course_content1'),  # http://127.0.0.1:8000/other/course_content1/
]

