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

    def test_comments_detail(self):
        response = self.client.get("/placeholder_api/comments_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
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
            )
        )

    def test_comments_search(self):
        response = self.client.get(
            "/placeholder_api/comments_search", query_params={"q": "ex"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 237)
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

    def test_comments_create(self):
        response = self.client.post(
            "/placeholder_api/comments_create",
            {
                "name": "new name",
                "email": "new@email.com",
                "body": "new body",
                "post": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_comments_update(self):
        response = self.client.put(
            "/placeholder_api/comments_update/1",
            {
                "name": "new name",
                "email": "new@email.com",
                "body": "new body",
                "post": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_comments_partial_update(self):
        response = self.client.patch(
            "/placeholder_api/comments_partial_update/1",
            {"name": "new name"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
