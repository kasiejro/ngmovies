from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'pk',
            'title',
        ]

    def validate_title(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("This title is too short")
        return value