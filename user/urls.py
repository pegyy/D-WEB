from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    path('login/',views.login,name='login'),
    path('register/',views.register, name='register'),
    path('panel/' , views.panel , name='panel'),
]