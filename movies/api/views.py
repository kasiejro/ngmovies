from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework import generics

from .serializers import  MovieSerializer,CommentSerializer
from movies.views import MovieRepository, OmdAPIClient, CommentRepository
from movies.models import Movie, Comment


class MovieCRUView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = []

    def get_queryset(self):
        qs = Movie.objects.all()
        query = self.request.GET.get("title")
        if query is not None:
            qs = qs.filter(title__iexact=query)
        return qs

    def post(self, request, *args, **kwargs):
        title = request.data.get("title")
        movie = OmdAPIClient.get_movie_or_none(title)

        if movie is not None:
            MovieRepository.upsert_movie(movie)
            return HttpResponse(movie.text)
        return HttpResponseNotFound("Movie not found in database.")


class CommentCRView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        movie_id = self.kwargs.get("movie_id")

        if movie_id is not None:
            return Comment.objects.filter(movie=movie_id)

        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        content = request.data.get("content")
        movie_id = request.data.get("movie")

        if len(content) > 0:
            new_comment = CommentRepository.save_comment(content, movie_id)
            if new_comment:
                return HttpResponse(new_comment)
            else:
                return HttpResponseBadRequest("Unable to create a new comment.")
        else:
            return HttpResponseBadRequest("No content was provided.")

    def get_serializer_context(self):
        return {'request' : self.request}