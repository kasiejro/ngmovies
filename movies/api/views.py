from django.http import HttpResponse, Http404
from rest_framework import generics, mixins

from .serializers import  MovieSerializer
from movies.views import get_movie_or_none
from movies.models import Movie


class MovieCRUView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = MovieSerializer
    permission_classes = []
    # queryset = Movie.objects.all()

    def get_queryset(self):
        return Movie.objects.all()

    def post(self, request, *args, **kwargs):
        title = request.POST["title"]
        response = get_movie_or_none(title)
        movie_instance = Movie.objects.filter(title__iexact=title)

        if movie_instance is not None:
            return HttpResponse(response)
        return HttpResponse("This movie does not exist in this database.")