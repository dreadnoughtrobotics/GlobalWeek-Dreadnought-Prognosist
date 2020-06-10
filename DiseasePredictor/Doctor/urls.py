from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Doctor'

urlpatterns = [
        url('^register/$', views.register, name="Registration"),
        ]