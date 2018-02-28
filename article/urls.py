from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.homepage),
    path('<int:article_id>/', views.detail, name='detail'),
    path('publish/', views.publish, name='publish'),
    path('update/<int:article_id>/', views.update, name='update'),
]
