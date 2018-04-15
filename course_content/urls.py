from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^(?P<pk>[0-9]+)/$', views.course_content,	name='course_content'),  # http://127.0.0.1:8000/course_content/1/

]
