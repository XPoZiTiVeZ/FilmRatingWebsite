from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('api/get_movies', get_movies, name="get_movies")
]
