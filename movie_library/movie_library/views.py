# from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie, Genre, Actor, Director

def homepage(request):
    # return HttpResponse('this is a homepage')
    template = 'homepage.html'
    return render(request, template)

def about(request):
    context = {
        'movies_count': Movie.objects.count(),
        'genres_count': Genre.objects.count(),
        'actors_count': Actor.objects.count(),
        'directors_count': Director.objects.count(),
    }
    return render(request, 'about.html', context)