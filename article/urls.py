from django.contrib import admin
from django.urls import path
from article.views import *

urlpatterns = [
    path(r'', article),
]
