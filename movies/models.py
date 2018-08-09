from django.db import models

from rest_framework.reverse import reverse as api_reverse


class Movie(models.Model):
    title = models.CharField(max_length=100)
    imdbID = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    plot = models.CharField(max_length=1024, null=True, blank=True)
    runtime = models.CharField(max_length=7, null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    writer = models.CharField(max_length=200, null=True, blank=True)
    actors = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    poster = models.CharField(max_length=200, null=True, blank=True)
    total_seasons = models.CharField(max_length=3, null=True, blank=True)
    rated = models.CharField(max_length=4, null=True, blank=True)
    released = models.CharField(max_length=20, null=True, blank=True)
    awards = models.CharField(max_length=50, null=True, blank=True)
    dvd = models.CharField(max_length=20, null=True, blank=True)
    boxoffice = models.CharField(max_length=20, null=True, blank=True)
    production = models.CharField(max_length=50, null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)

class Comment(models.Model):
    content = models.CharField(max_length=600)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def get_api_url(self, request=None):
        return api_reverse("api-movies:movie-comment-r", kwargs={'movie_id' : self.pk}, request=request)