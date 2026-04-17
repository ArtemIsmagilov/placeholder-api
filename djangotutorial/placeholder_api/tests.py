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

    def test_comments_filter(self):
        response = self.client.get(
            "/placeholder_api/comments_filter", query_params={"post": 1}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 5)
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

    def test_comments_delete(self):
        response = self.client.delete("/placeholder_api/comments_delete/500")
        self.assertEqual(response.status_code, 200)

    def test_users_filter(self):
        response = self.client.get(
            "/placeholder_api/users_filter", query_params={"id": 1}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 1)
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
                            "username": {"type": "string"},
                            "email": {"type": "string"},
                            "address": {"type": "string"},
                            "phone": {"type": "string"},
                            "website": {"type": "string"},
                            "company": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "name",
                            "username",
                            "email",
                            "address",
                            "phone",
                            "website",
                            "company",
                        ],
                    },
                },
            )
        )

    def test_users_delete(self):
        response = self.client.delete("/placeholder_api/users_delete/500")
        self.assertEqual(response.status_code, 200)

    def test_users_list(self):
        response = self.client.get("/placeholder_api/users_list")
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
                            "username": {"type": "string"},
                            "email": {"type": "string"},
                            "address": {"type": "string"},
                            "phone": {"type": "string"},
                            "website": {"type": "string"},
                            "company": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "name",
                            "username",
                            "email",
                            "address",
                            "phone",
                            "website",
                            "company",
                        ],
                    },
                },
            )
        )

    def test_users_detail(self):
        response = self.client.get("/placeholder_api/users_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "address": {"type": "string"},
                        "phone": {"type": "string"},
                        "website": {"type": "string"},
                        "company": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "name",
                        "username",
                        "email",
                        "address",
                        "phone",
                        "website",
                        "company",
                    ],
                },
            )
        )

    def test_users_search(self):
        response = self.client.get(
            "/placeholder_api/users_search", query_params={"q": "Graham"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 1)
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
                            "username": {"type": "string"},
                            "email": {"type": "string"},
                            "address": {"type": "string"},
                            "phone": {"type": "string"},
                            "website": {"type": "string"},
                            "company": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "name",
                            "username",
                            "email",
                            "address",
                            "phone",
                            "website",
                            "company",
                        ],
                    },
                },
            )
        )

    def test_users_create(self):
        response = self.client.post(
            "/placeholder_api/users_create",
            {
                "name": "new name",
                "username": "newusername",
                "email": "new@email.com",
                "address": "new address",
                "phone": "123456",
                "website": "newsite.com",
                "company": "New Company",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_users_update(self):
        response = self.client.put(
            "/placeholder_api/users_update/1",
            {
                "name": "updated name",
                "username": "updatedusername",
                "email": "updated@email.com",
                "address": "updated address",
                "phone": "654321",
                "website": "updatedsite.com",
                "company": "Updated Company",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_users_partial_update(self):
        response = self.client.patch(
            "/placeholder_api/users_partial_update/1",
            {"name": "patched name"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_todos_list(self):
        response = self.client.get("/placeholder_api/todos_list")
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
                            "title": {"type": "string"},
                            "completed": {"type": "boolean"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "completed", "user"],
                    },
                },
            )
        )

    def test_todos_detail(self):
        response = self.client.get("/placeholder_api/todos_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "completed": {"type": "boolean"},
                        "user": {"type": "number"},
                    },
                    "required": ["id", "title", "completed", "user"],
                },
            )
        )

    def test_todos_search(self):
        response = self.client.get(
            "/placeholder_api/todos_search", query_params={"q": "dolor"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 36)
        self.assertIsNone(
            jsonschema.validate(
                response.json()["results"],
                {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "title": {"type": "string"},
                            "completed": {"type": "boolean"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "completed", "user"],
                    },
                },
            )
        )

    def test_todos_create(self):
        response = self.client.post(
            "/placeholder_api/todos_create",
            {"title": "new todo", "completed": False, "user": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_todos_update(self):
        response = self.client.put(
            "/placeholder_api/todos_update/1",
            {"title": "updated todo", "completed": True, "user": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_todos_partial_update(self):
        response = self.client.patch(
            "/placeholder_api/todos_partial_update/1",
            {"title": "patched todo"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_todos_filter(self):
        response = self.client.get(
            "/placeholder_api/todos_filter", query_params={"user": 1}
        )
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
                            "title": {"type": "string"},
                            "completed": {"type": "boolean"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "completed", "user"],
                    },
                },
            )
        )

    def test_todos_delete(self):
        response = self.client.delete("/placeholder_api/todos_delete/500")
        self.assertEqual(response.status_code, 200)

    def test_albums_list(self):
        response = self.client.get("/placeholder_api/albums_list")
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
                            "title": {"type": "string"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "user"],
                    },
                },
            )
        )

    def test_albums_detail(self):
        response = self.client.get("/placeholder_api/albums_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "user": {"type": "number"},
                    },
                    "required": ["id", "title", "user"],
                },
            )
        )

    def test_albums_search(self):
        response = self.client.get(
            "/placeholder_api/albums_search", query_params={"q": "qu"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 66)
        self.assertIsNone(
            jsonschema.validate(
                response.json()["results"],
                {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "title": {"type": "string"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "user"],
                    },
                },
            )
        )

    def test_albums_create(self):
        response = self.client.post(
            "/placeholder_api/albums_create",
            {"title": "new album", "user": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_albums_update(self):
        response = self.client.put(
            "/placeholder_api/albums_update/1",
            {"title": "updated album", "user": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_albums_partial_update(self):
        response = self.client.patch(
            "/placeholder_api/albums_partial_update/1",
            {"title": "patched album"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_albums_filter(self):
        response = self.client.get(
            "/placeholder_api/albums_filter", query_params={"user": 1}
        )
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
                            "title": {"type": "string"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "user"],
                    },
                },
            )
        )

    def test_albums_delete(self):
        response = self.client.delete("/placeholder_api/albums_delete/500")
        self.assertEqual(response.status_code, 200)

    def test_photos_list(self):
        response = self.client.get("/placeholder_api/photos_list")
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
                            "title": {"type": "string"},
                            "url": {"type": "string"},
                            "thumbnail_url": {"type": "string"},
                            "album": {"type": "number"},
                        },
                        "required": ["id", "title", "url", "thumbnail_url", "album"],
                    },
                },
            )
        )

    def test_photos_detail(self):
        response = self.client.get("/placeholder_api/photos_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "url": {"type": "string"},
                        "thumbnail_url": {"type": "string"},
                        "album": {"type": "number"},
                    },
                    "required": ["id", "title", "url", "thumbnail_url", "album"],
                },
            )
        )

    def test_photos_search(self):
        response = self.client.get(
            "/placeholder_api/photos_search", query_params={"q": "lorem"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 355)
        self.assertIsNone(
            jsonschema.validate(
                response.json()["results"],
                {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "title": {"type": "string"},
                            "url": {"type": "string"},
                            "thumbnail_url": {"type": "string"},
                            "album": {"type": "number"},
                        },
                        "required": ["id", "title", "url", "thumbnail_url", "album"],
                    },
                },
            )
        )

    def test_photos_create(self):
        response = self.client.post(
            "/placeholder_api/photos_create",
            {
                "title": "new photo",
                "url": "https://example.com/photo.jpg",
                "thumbnail_url": "https://example.com/thumb.jpg",
                "album": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_photos_update(self):
        response = self.client.put(
            "/placeholder_api/photos_update/1",
            {
                "title": "updated photo",
                "url": "https://example.com/updated.jpg",
                "thumbnail_url": "https://example.com/updated_thumb.jpg",
                "album": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_photos_partial_update(self):
        response = self.client.patch(
            "/placeholder_api/photos_partial_update/1",
            {"title": "patched photo"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_photos_filter(self):
        response = self.client.get(
            "/placeholder_api/photos_filter", query_params={"album": 1}
        )
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
                            "title": {"type": "string"},
                            "url": {"type": "string"},
                            "thumbnail_url": {"type": "string"},
                            "album": {"type": "number"},
                        },
                        "required": ["id", "title", "url", "thumbnail_url", "album"],
                    },
                },
            )
        )

    def test_photos_delete(self):
        response = self.client.delete("/placeholder_api/photos_delete/500")
        self.assertEqual(response.status_code, 200)

    def test_posts_list(self):
        response = self.client.get("/placeholder_api/posts_list")
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
                            "title": {"type": "string"},
                            "body": {"type": "string"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "body", "user"],
                    },
                },
            )
        )

    def test_posts_detail(self):
        response = self.client.get("/placeholder_api/posts_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "user": {"type": "number"},
                    },
                    "required": ["id", "title", "body", "user"],
                },
            )
        )

    def test_posts_search(self):
        response = self.client.get(
            "/placeholder_api/posts_search", query_params={"q": "sunt"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 23)
        self.assertIsNone(
            jsonschema.validate(
                response.json()["results"],
                {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "title": {"type": "string"},
                            "body": {"type": "string"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "body", "user"],
                    },
                },
            )
        )

    def test_posts_create(self):
        response = self.client.post(
            "/placeholder_api/posts_create",
            {"title": "new post", "body": "new body", "user": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_posts_update(self):
        response = self.client.put(
            "/placeholder_api/posts_update/1",
            {"title": "updated post", "body": "updated body", "user": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_posts_partial_update(self):
        response = self.client.patch(
            "/placeholder_api/posts_partial_update/1",
            {"title": "patched post"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_posts_filter(self):
        response = self.client.get(
            "/placeholder_api/posts_filter", query_params={"user": 1}
        )
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
                            "title": {"type": "string"},
                            "body": {"type": "string"},
                            "user": {"type": "number"},
                        },
                        "required": ["id", "title", "body", "user"],
                    },
                },
            )
        )

    def test_posts_delete(self):
        response = self.client.delete("/placeholder_api/posts_delete/500")
        self.assertEqual(response.status_code, 200)
