from django.http import HttpResponse, Http404
from rest_framework import generics, mixins

from .serializers import  MovieSerializer
from movies.views import get_movie_or_none, save_movie
from movies.models import Movie


class MovieCRUView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = MovieSerializer
    permission_classes = []
    # queryset = Movie.objects.all()

    def get_queryset(self):
        return Movie.objects.all()

    def post(self, request, *args, **kwargs):
        title = request.POST["title"]
        movie = get_movie_or_none(title)

        if movie is not None:
            save_movie(movie)
            return HttpResponse(movie.text)
        return HttpResponse("This movie does not exist in this database.")