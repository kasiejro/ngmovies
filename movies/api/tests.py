from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse


from movies.models import Movie, Comment


class MovieAPITestCase(APITestCase):
    def setUp(self):
        movie_obj = Movie(title='test')
        movie_obj.save()

    def test_single_movie(self):
        movie_count = Movie.objects.count()
        self.assertEqual(movie_count, 1)

    def test_get_movies(self):
        data = {}
        url = api_reverse("api-movies:movie-cru")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_movie(self):
        data = {'title' : 'Avatar'}
        url = api_reverse("api-movies:movie-cru")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_not_existant_movie(self):
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

    def test_comment_count(self):
        comment_count = Comment.objects.count()
        self.assertEqual(comment_count, 1)

    def test_get_comments(self):
        data = {}
        url = api_reverse("api-movies:comment-cr")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comments(self):
        data = {'content' : 'random content', 'movie' : '1'}
        url = api_reverse("api-movies:comment-cr")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comments_no_content(self):
        data = {'content' : '', 'movie' : '1'}
        url = api_reverse("api-movies:comment-cr")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # TODO poprawić test
    # def test_post_comments_no_movie(self):
    #     data = {'content' : 'random content', 'movie' : '999999'}
    #     url = api_reverse("api-movies:comment-cr")
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # TODO poprawić test
    # def test_get_comments_body(self):
    #     data = {}
    #     url = api_reverse("api-movies:comment-cr")
    #     response = self.client.get(url, data, format='json')
    #     self.assertEqual(response.data, Comment.objects.all() )