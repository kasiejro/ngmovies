import requests

from movies.models import Movie

API_URL = 'http://www.omdbapi.com'
API_KEY = 'ffbdeb5c'


def get_movie_or_none(title):
    payload = {'t' : title, 'apikey' : API_KEY}
    r = requests.get(API_URL, params=payload)
    if r.json()["Response"] == 'True':
        return r
    return None

def save_movie(movie):
    movie = movie.json()
    movie_instance = Movie.objects.filter(title__iexact=movie["Title"])

    if movie_instance:
        movie_instance = movie_instance[0]
    else:
        movie_instance = Movie()

    movie_instance.year = movie["Year"]
    movie_instance.imdbID = movie["imdbID"]
    movie_instance.plot = movie["Plot"]
    movie_instance.runtime = movie["Runtime"]
    movie_instance.writer = movie["Writer"]
    movie_instance.actors = movie["Actors"]
    movie_instance.language = movie["Language"]
    movie_instance.country = movie["Country"]
    movie_instance.type = movie["Type"]
    movie_instance.title = movie["Title"]
    movie_instance.genre = movie["Genre"]
    movie_instance.director = movie["Director"]
    movie_instance.poster = movie["Poster"]
    if movie["Type"] == "movie":
        pass
    elif movie["Type"] == "series":
        movie_instance.total_seasons = movie["totalSeasons"]


    movie_instance.save()


