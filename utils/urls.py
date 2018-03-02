from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('check_code/', views.create_code_img, name='create_code_img'),
]
