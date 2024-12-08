from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    path('adlogin/',views.adlogin,name='adlogin'),
    path('management/',views.management , name='management'),
]