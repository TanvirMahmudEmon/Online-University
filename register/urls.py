from django.conf.urls import include, url

from register.views import course,reg,login1


urlpatterns = [
    url(r'^reg/$', reg, name='reg'),
    url(r'^course/$', course, name='course'),
    url(r'^login1/$', login1, name='login1'),
]

