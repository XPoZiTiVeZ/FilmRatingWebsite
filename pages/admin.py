from django.contrib import admin
from .models import Movie, Movie_link, Movie_dup_title, Movie_tag

admin.site.register(Movie)
admin.site.register(Movie_link)
admin.site.register(Movie_dup_title)
admin.site.register(Movie_tag)