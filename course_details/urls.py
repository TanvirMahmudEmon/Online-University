from django.conf.urls import url

from . import views

urlpatterns=[

    url(r'^(?P<pk>[0-9]+)/$', views.course_details,	name='course_details'),  # http://127.0.0.1:8000/course_details/1/

]
