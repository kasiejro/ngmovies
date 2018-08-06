from rest_framework import generics

from .serializers import  MovieSerializer
from movies.models import Movie


class MovieCRUView(generics.RetrieveUpdateAPIView):
    lookup_field = 'title'
    serializer_class = MovieSerializer
    # queryset = Movie.objects.all()

    def get_queryset(self):
        return Movie.objects.all()