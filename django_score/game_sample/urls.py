from django.conf import settings
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]

if settings.DEBUG:
    urlpatterns.append(url(r'^ping/', views.pong))
