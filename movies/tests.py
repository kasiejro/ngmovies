from django.test import TestCase

from movies.views import CommentRepository
from .models import Movie, Comment


class CommentRepositoryTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="lion")

    def test_saving_comment(self, content = "qwerty", movie_id="1"):
        comment = CommentRepository.save_comment(content, movie_id)
        db_comment = Comment.objects.get(movie_id=movie_id)
        self.assertEqual(comment, db_comment)