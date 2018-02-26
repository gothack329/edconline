from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.homepage),
    path('<int:article_id>/', views.detail, name='detail'),
]
