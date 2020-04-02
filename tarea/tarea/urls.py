"""tarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path, include
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

from login.views import LoginClass,l
print("urls py")
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',LandingClass.as_view(), name = 'landing'),
    path('', include('Landing.urls')),    
    path('login/',include('login.urls'), name='login'),
    path('Dashboard/',include('Dashboard.urls'),name='Dashboard'),
    path('logout/',l.as_view() ,name ='logout'),
    path('registro/',include('Register.urls'),name='Register')
]
