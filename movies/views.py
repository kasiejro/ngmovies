import requests

API_URL = 'http://www.omdbapi.com'
API_KEY = 'ffbdeb5c'


def get_movie_or_none(title):
    payload = {'t' : title, 'apikey' : API_KEY}
    r = requests.get(API_URL, params=payload)
    if "title" in r.text.lower():
        return r.text
    return None

