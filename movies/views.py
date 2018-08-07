import requests

from movies.models import Movie, Comment

API_URL = 'http://www.omdbapi.com'
API_KEY = 'ffbdeb5c'

class OmdAPIClient:

    @staticmethod
    def get_movie_or_none(title):
        payload = {'t' : title, 'apikey' : API_KEY}
        r = requests.get(API_URL, params=payload)

        try:
            response = r.json()["Response"]
        except ValueError:
            print("Couldn't parse to json")

        if  response == 'True':
            return r
        return None

class MovieRepository:

    @staticmethod
    def upsert_movie(movie_from_api):
        api_response = movie_from_api.json()
        movie_instance = Movie.objects.filter(title__iexact=api_response["Title"])

        if movie_instance:
            movie_instance = movie_instance[0]
        else:
            movie_instance = Movie()

            map_response_to_movie(movie_instance, api_response)
        movie_instance.save()


class CommentRepository:

    @staticmethod
    def save_comment(content, movie_id):
        movie = Movie.objects.get(pk=movie_id)

        new_comment = Comment()
        new_comment.movie = movie
        new_comment.content = content
        new_comment.save()

        return  new_comment


def map_response_to_movie(movie_instance, api_response):
    movie_instance.year = api_response["Year"]
    movie_instance.imdbID = api_response["imdbID"]
    movie_instance.plot = api_response["Plot"]
    movie_instance.runtime = api_response["Runtime"]
    movie_instance.writer = api_response["Writer"]
    movie_instance.actors = api_response["Actors"]
    movie_instance.language = api_response["Language"]
    movie_instance.country = api_response["Country"]
    movie_instance.type = api_response["Type"]
    movie_instance.title = api_response["Title"]
    movie_instance.genre = api_response["Genre"]
    movie_instance.director = api_response["Director"]
    movie_instance.awards = api_response["Awards"]
    movie_instance.rated = api_response["Rated"]
    movie_instance.released = api_response["Released"]
    if api_response["Type"] == "movie":
        movie_instance.dvd = api_response["DVD"]
        movie_instance.boxoffice = api_response["BoxOffice"]
        movie_instance.production = api_response["Production"]
        movie_instance.website = api_response["Website"]
    elif api_response["Type"] == "series":
        movie_instance.total_seasons = api_response["totalSeasons"]