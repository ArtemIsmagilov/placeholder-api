from django.test import TestCase
from django.test import Client
import jsonschema

from .models import Comment, Todo, Album, User, Photo, Post


# Create your tests here.
class PlaceholderApiTestCase(TestCase):
    fixtures = ["f.json"]
    client = Client()

    def test_comments(self):
        self.assertEqual(Comment.objects.count(), 500)

    def test_todos(self):
        self.assertEqual(Todo.objects.count(), 200)

    def test_albums(self):
        self.assertEqual(Album.objects.count(), 100)

    def test_photos(self):
        self.assertEqual(Photo.objects.count(), 5000)

    def test_posts(self):
        self.assertEqual(Post.objects.count(), 100)

    def test_users(self):
        self.assertEqual(User.objects.count(), 10)

    def test_comments_list(self):
        response = self.client.get("/placeholder_api/comments_list")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json()["results"],
                {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "name": {"type": "string"},
                            "email": {"type": "string"},
                            "body": {"type": "string"},
                            "post": {"type": "number"},
                        },
                        "required": ["id", "name", "email", "body", "post"],
                    },
                },
            )
        )
