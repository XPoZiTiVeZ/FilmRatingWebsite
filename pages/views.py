from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse


from .models import Movie, Movie_link, Movie_image


from json import dumps
import os


def remove_symbols(string: str, symbols: str):
    for s in symbols:
        string = string.replace(s, "")
    return string.replace("  ", " ")

def index(request):
    context = {}
    context["movies"] = Movie.objects.all()[:30]
    # sorted(Movie.objects.all(), key=lambda movie: movie.links.all()[0].origin)
    # print(context["movies"])
    
    return render(request, 'pages/index.djt', context)

@require_POST
def get_movies(request):
    index = int(request.POST.get("index"))
    
    data = dict()
    data["update"] = [
        {
            "title": movie.title,
            "description": movie.description,
            "translit_title": movie.translit_title,
            "links": [
                {
                    "link": link.link,
                    "origin": link.origin
                } for link in movie.links.all()
            ],
            "images": [
                image.image.name for image in movie.images.all()
            ]
        } for movie in Movie.objects.all()[index:index+20]
    ]

    return HttpResponse(dumps(data))