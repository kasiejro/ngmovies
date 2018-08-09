# ngmovies - simple REST API for movie database
This project uses http://omdbapi.com.

Basic requirements: Python 3.7.0 and Django 2.1
pip3 install requirements - for installing all project requirements

python manage.py runserver - for opening the application locally

The app can be found live at https://ngmovies-kr.herokuapp.com/

Endpoints for:
Comments - /api/comments/
Movies - /api/movies/

Examples:
* Get all movies from database: GET /api/movies/ 
* Get movie under a given title from database: GET /api/movies/?title=Avatar
* Insert or update movie under given title in the database and return API response: POST /api/movies/ params={"title":"Avatar"}

* Get all comments from database: GET /api/comments/
* Get all comments assigned to a movie under specific id from database: GET /api/comments/<id> eg. /api/comments/1
* Create a comment assigned to a secific movie and insert it to database and return the Comment object: POST /api/comments/ {"content":"random comment", "movie":"1"}
