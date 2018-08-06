import requests

API_URL = 'http://www.omdbapi.com'
API_KEY = 'ffbdeb5c'


def get_movie_from_api(title):
    payload = {'t' : title, 'apikey' : API_KEY}
    r = requests.get(API_URL, params=payload)
    return requests.get(API_URL, params=payload).text

