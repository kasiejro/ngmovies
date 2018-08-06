from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'pk',
            'title',
            'imdbID',
            'type',
            'year',
            'runtime',
            'genre',
            'director',
            'writer',
            'actors',
            'language',
            'country',
            'poster',
            'total_seasons',
            'plot',
        ]
        read_only_fields = ['pk']

    def validate_title(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("This title is too short")
        return value