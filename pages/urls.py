from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('api/get_movies', get_movies, name="get_movies"),
    path('api/get_movie', get_movie, name="get_movie"),
]
