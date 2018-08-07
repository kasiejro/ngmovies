from django.conf.urls import url

from .views import MovieCRUView, CommentCRView

app_name = 'movies'

urlpatterns = [
    url(r'^movies/$', MovieCRUView.as_view(), name='movie-cru'),
    url(r'^comments/$', CommentCRView.as_view(), name='comment-cr'),
    url(r'^comments/(?P<movie_id>[0-9])/$', CommentCRView.as_view(), name='movie-comment-r'),
]
