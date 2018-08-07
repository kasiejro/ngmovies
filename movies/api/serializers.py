from rest_framework import serializers

from movies.models import Movie,Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'imdbID',
            'type',
            'year',
            'plot',
            'runtime',
            'genre',
            'director',
            'writer',
            'actors',
            'language',
            'country',
            'poster',
            'total_seasons',
            'rated',
            'released',
            'awards',
            'dvd',
            'boxoffice',
            'production',
            'website',
        ]

    def validate_title(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("This title is too short")
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'movie',
            'content',
        ]

    def validate_movie_id(self, value):
        movie = Movie.objects.exists(pk=value)
        if movie:
            return value
        else:
            raise serializers.ValidationError("There is no movie under this id")

    def validate_content(self, value):
        #not empty
        pass