from django.urls import include, re_path,path 
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_view
from login.views import LoginClass

app_name = 'login'

urlpatterns = [
    path('',LoginClass.as_view(), name = 'login'),
]