from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('member/<str:username>/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
]
