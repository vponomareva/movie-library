from django.contrib import admin

from .models import Genre, Director, Actor, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'get_genres', 'get_directors']
    list_filter = ['release_year', 'genres']
    search_fields = ['title', 'description']
    filter_horizontal = ['genres', 'directors', 'actors']
    
    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    get_genres.short_description = 'Жанры'
    
    def get_directors(self, obj):
        return ", ".join([director.name for director in obj.directors.all()])
    get_directors.short_description = 'Режиссеры'