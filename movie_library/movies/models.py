from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)

    class Meta:
        verbose_name = 'режиссер'
        verbose_name_plural = 'режиссеры'

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)

    class Meta:
        verbose_name = 'актер'
        verbose_name_plural = 'актеры'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    release_year = models.IntegerField(
        verbose_name='Год премьеры',
        validators=[
            MinValueValidator(1888, message='Первый фильм был снят в 1888 году'),
            MaxValueValidator(
                datetime.now().year + 1,
                message='Год не может быть в будущем'
            )
        ]
    )
    poster = models.ImageField(
        verbose_name='Постер',
        upload_to='posters/',
        blank=True,
        null=True,
    )
    duration = models.IntegerField(
        verbose_name='Длительность (мин)',
        blank=True,
        null=True,
        help_text='Длительность в минутах'
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length=50,
        blank=True,
        null=True
    )

    directors = models.ManyToManyField(
        Director,
        related_name='directed_movies',
        verbose_name='Режиссеры'
    )
    actors = models.ManyToManyField(
        Actor,
        related_name='acted_movies',
        verbose_name='Актеры'
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='genre_movies',
        verbose_name='Жанры'
    )

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
        ordering = ['-release_year', 'title']

    def __str__(self):
        return f"{self.title} ({self.release_year})"
