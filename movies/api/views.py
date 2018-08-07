from django.http import HttpResponse
from rest_framework import generics

from .serializers import  MovieSerializer,CommentSerializer
from movies.views import get_movie_or_none, save_movie
from movies.models import Movie, Comment


class MovieCRUView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = []

    def get_queryset(self):
        return Movie.objects.all()

    def post(self, request, *args, **kwargs):
        title = request.POST.get(key="t")
        movie = get_movie_or_none(title)

        if movie is not None:
            save_movie(movie)
            return HttpResponse(movie.text)
        return HttpResponse("This movie does not exist in this database.")


class CommentCRView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = []

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        pass