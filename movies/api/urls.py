from django.conf.urls import url

from .views import MovieCRUView

app_name = 'movies'

urlpatterns = [
    url(r'^$', MovieCRUView.as_view(), name='movie-cru'),
]
