from rest_framework import serializers


from movies.models import Movie,Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'pk',
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
            raise serializers.ValidationError("This title is too short", 400)
        return value


class CommentSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'movie',
            'content',
            'uri',
        ]

    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_movie(self, value):
        movie = Movie.objects.exists(pk=value)
        if movie:
            return value
        else:
            raise serializers.ValidationError("There is no movie under this id", 400)

    def validate_content(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("No content was provided.", 400)
        return value