from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Movie

NUM_MOVIES_PAGE = 6


def movie_list(request):
    template_name = 'movies/list.html'
    movies = Movie.objects.all()
    search = request.GET.get('search', '')

    if search:
        movies = movies.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )
    
    paginator = Paginator(movies, NUM_MOVIES_PAGE)
    page = request.GET.get('page')
    movies_page = paginator.get_page(page)

    context = {
        'movies': movies_page,
        # 'movies': movies,
        'search_query': search,
    }
    return render(request, template_name, context)


def movie_detail(request, movie_id):
    template_name = 'movies/detail.html'
    movie = Movie.objects.get(id=movie_id)
    context = {
        'movie': movie
    }
    return render(request, template_name, context)
