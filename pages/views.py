from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse

from .models import Movie, Movie_link, Movie_image

from json import dumps


def remove_symbols(string: str, symbols: str):
    for s in symbols:
        string = string.replace(s, "")
    return string.replace("  ", " ")

def index(request):
    context = {}
    context["movies"] = Movie.objects.all()[:30]
    # sorted(Movie.objects.all(), key=lambda movie: movie.links.all()[0].origin)
    # print(context["movies"])
    
    return render(request, 'pages/index.jinja', context)

@require_POST
def get_movies(request):
    index = int(request.POST.get("index"))
    
    data = dict()
    data["update"] = [
        {   
            "id": movie.id,
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

@require_POST
def get_movie(request):
    movie_id: str = request.POST.get("movie_id")
    
    data = dict()
    if not movie_id.isdigit():
        data["status"] = 400
        return HttpResponse(dumps(data))
    
    movie = Movie.objects.filter(id = movie_id).first()  
    data["movie"] = {
        "id": movie.id,
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
    }
    data["status"] = 200

    return HttpResponse(dumps(data))