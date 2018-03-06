from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('member/<str:username>/', views.profile, name='profile'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('register/', views.register, name='register'),
    path('change_password/', views.password_change, name='password_change'),
]
