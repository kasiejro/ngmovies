import json

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse


from movies.models import Movie, Comment


class MovieAPITestCase(APITestCase):
    def setUp(self):
        movie_obj = Movie(title='test')
        movie_obj.save()

    def test_get_movies(self):
        """Getting movies from database"""
        data = {}
        url = api_reverse("api-movies:movie-cru")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_movie(self):
        """Adding movie from external API to database"""
        data = {'title' : 'Avatar'}
        url = api_reverse("api-movies:movie-cru")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_not_existant_movie(self):
        """Trying to add unexisting movie from external API to database"""
        data = {'title' : 'qwertyuiop'}
        url = api_reverse("api-movies:movie-cru")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CommentAPITestCase(APITestCase):
    def setUp(self):
        movie_obj = Movie(title='test')
        movie_obj.save()

        comment_obj = Comment(content='test content', movie=movie_obj)
        comment_obj.save()

    def test_get_comments(self):
        """Get comment list"""
        data = {}
        url = api_reverse("api-movies:comment-cr")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comments(self):
        """Instert or update of a movie """
        data = {'content' : 'random content', 'movie' : '1'}
        url = api_reverse("api-movies:comment-cr")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_comments_no_content(self):
        ''' Add comment to the movie - empty content'''
        data = {'content' : '', 'movie' : '1'}
        url = api_reverse("api-movies:comment-cr")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_comments_no_movie(self):
        ''' Add comment to the movie - unexisting movie id'''
        data = {'content' : 'random content', 'movie' : '999999'}
        url = api_reverse("api-movies:comment-cr")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_movie_comments(self):
        '''Get all comments belonging to certain movie'''
        data = {}
        url = api_reverse("api-movies:movie-comment-r", kwargs={"movie_id" : "1"})
        response = self.client.get(url, data, format='json').content
        movie_comments =  b'[{"movie":1,"content":"test content","uri":"http://testserver/api/comments/1/"}]'
        self.assertEqual(response, movie_comments)
