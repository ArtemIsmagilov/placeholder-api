from django.test import TestCase, Client
from django.conf import settings
import jsonschema

from .models import User, Chat, Message


class ChatsApiTestCase(TestCase):
    fixtures = ["chats.json"]
    client = Client()

    def test_users(self):
        self.assertEqual(User.objects.count(), 10)

    def test_chats(self):
        self.assertEqual(Chat.objects.count(), 100)

    def test_messages(self):
        self.assertEqual(Message.objects.count(), 1000)

    def test_users_list(self):
        response = self.client.get("/chats_api/users_list")
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
                            "username": {"type": "string"},
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "username", "created_at"],
                    },
                },
            )
        )

    def test_users_detail(self):
        response = self.client.get("/chats_api/users_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "username": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["id", "username", "created_at"],
                },
            )
        )

    def test_users_search(self):
        response = self.client.get(
            "/chats_api/users_search", query_params={"q": "user 0"}
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
                            "username": {"type": "string"},
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "username", "created_at"],
                    },
                },
            )
        )

    def test_users_create(self):
        response = self.client.post(
            "/chats_api/users_create",
            {"username": "new user"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_users_create_forbidden(self):
        response = self.client.post(
            "/chats_api/users_create",
            {"username": "new user"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_users_update(self):
        response = self.client.put(
            "/chats_api/users_update/1",
            {"username": "updated user"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_users_update_forbidden(self):
        response = self.client.put(
            "/chats_api/users_update/1",
            {"username": "updated user"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_users_partial_update(self):
        response = self.client.patch(
            "/chats_api/users_partial_update/1",
            {"username": "patched user"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_users_partial_update_forbidden(self):
        response = self.client.patch(
            "/chats_api/users_partial_update/1",
            {"username": "patched user"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_users_filter(self):
        response = self.client.get("/chats_api/users_filter", query_params={"id": 1})
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
                            "username": {"type": "string"},
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "username", "created_at"],
                    },
                },
            )
        )

    def test_users_delete(self):
        response = self.client.delete(
            "/chats_api/users_delete/10",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_users_delete_forbidden(self):
        response = self.client.delete(
            "/chats_api/users_delete/10",
        )
        self.assertEqual(response.status_code, 403)

    def test_chats_list(self):
        response = self.client.get("/chats_api/chats_list")
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
                            "users": {
                                "type": "array",
                                "items": {"type": "number"},
                            },
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "name", "users", "created_at"],
                    },
                },
            )
        )

    def test_chats_detail(self):
        response = self.client.get("/chats_api/chats_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "users": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "created_at": {"type": "string"},
                    },
                    "required": ["id", "name", "users", "created_at"],
                },
            )
        )

    def test_chats_search(self):
        response = self.client.get(
            "/chats_api/chats_search", query_params={"q": "chat 0"}
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
                            "users": {
                                "type": "array",
                                "items": {"type": "number"},
                            },
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "name", "users", "created_at"],
                    },
                },
            )
        )

    def test_chats_create(self):
        response = self.client.post(
            "/chats_api/chats_create",
            {"name": "new chat", "users": [1, 2]},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_chats_create_forbidden(self):
        response = self.client.post(
            "/chats_api/chats_create",
            {"name": "new chat", "users": [1, 2]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_chats_update(self):
        response = self.client.put(
            "/chats_api/chats_update/1",
            {"name": "updated chat", "users": [1, 3]},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_chats_update_forbidden(self):
        response = self.client.put(
            "/chats_api/chats_update/1",
            {"name": "updated chat", "users": [1, 3]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_chats_partial_update(self):
        response = self.client.patch(
            "/chats_api/chats_partial_update/1",
            {"name": "patched chat"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_chats_partial_update_forbidden(self):
        response = self.client.patch(
            "/chats_api/chats_partial_update/1",
            {"name": "patched chat"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_chats_filter(self):
        response = self.client.get("/chats_api/chats_filter", query_params={"id": 1})
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
                            "users": {
                                "type": "array",
                                "items": {"type": "number"},
                            },
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "name", "users", "created_at"],
                    },
                },
            )
        )

    def test_chats_delete(self):
        response = self.client.delete(
            "/chats_api/chats_delete/10",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_chats_delete_forbidden(self):
        response = self.client.delete(
            "/chats_api/chats_delete/10",
        )
        self.assertEqual(response.status_code, 403)

    def test_messages_list(self):
        response = self.client.get("/chats_api/messages_list")
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
                            "chat": {"type": "number"},
                            "author": {"type": "number"},
                            "text": {"type": "string"},
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "chat", "author", "text", "created_at"],
                    },
                },
            )
        )

    def test_messages_detail(self):
        response = self.client.get("/chats_api/messages_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "chat": {"type": "number"},
                        "author": {"type": "number"},
                        "text": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["id", "chat", "author", "text", "created_at"],
                },
            )
        )

    def test_messages_search(self):
        response = self.client.get(
            "/chats_api/messages_search", query_params={"q": "message"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 1000)
        self.assertIsNone(
            jsonschema.validate(
                response.json()["results"],
                {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "chat": {"type": "number"},
                            "author": {"type": "number"},
                            "text": {"type": "string"},
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "chat", "author", "text", "created_at"],
                    },
                },
            )
        )

    def test_messages_create(self):
        response = self.client.post(
            "/chats_api/messages_create",
            {"chat": 1, "author": 1, "text": "new message"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_messages_create_forbidden(self):
        response = self.client.post(
            "/chats_api/messages_create",
            {"chat": 1, "author": 1, "text": "new message"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_messages_update(self):
        response = self.client.put(
            "/chats_api/messages_update/1",
            {"chat": 1, "author": 1, "text": "updated message"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_messages_update_forbidden(self):
        response = self.client.put(
            "/chats_api/messages_update/1",
            {"chat": 1, "author": 1, "text": "updated message"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_messages_partial_update(self):
        response = self.client.patch(
            "/chats_api/messages_partial_update/1",
            {"text": "patched message"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_messages_partial_update_forbidden(self):
        response = self.client.patch(
            "/chats_api/messages_partial_update/1",
            {"text": "patched message"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_messages_filter(self):
        response = self.client.get(
            "/chats_api/messages_filter", query_params={"chat": 1}
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
                            "chat": {"type": "number"},
                            "author": {"type": "number"},
                            "text": {"type": "string"},
                            "created_at": {"type": "string"},
                        },
                        "required": ["id", "chat", "author", "text", "created_at"],
                    },
                },
            )
        )

    def test_messages_delete(self):
        response = self.client.delete(
            "/chats_api/messages_delete/100",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_messages_delete_forbidden(self):
        response = self.client.delete(
            "/chats_api/messages_delete/100",
        )
        self.assertEqual(response.status_code, 403)

    def test_profile(self):
        response = self.client.get("/chats_api/profile/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "user_info": {
                            "type": "object",
                            "properties": {
                                "username": {"type": "string"},
                                "created_at": {"type": "string"},
                            },
                            "required": ["username", "created_at"],
                        },
                        "chats": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "number"},
                                    "name": {"type": "string"},
                                    "created_at": {"type": "string"},
                                    "users": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "number"},
                                                "username": {"type": "string"},
                                            },
                                            "required": ["id", "username"],
                                        },
                                    },
                                    "messages": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "number"},
                                                "text": {"type": "string"},
                                                "created_at": {"type": "string"},
                                                "author": {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {"type": "number"},
                                                        "username": {"type": "string"},
                                                    },
                                                    "required": ["id", "username"],
                                                },
                                            },
                                            "required": [
                                                "id",
                                                "text",
                                                "created_at",
                                                "author",
                                            ],
                                        },
                                    },
                                },
                                "required": [
                                    "id",
                                    "name",
                                    "created_at",
                                    "users",
                                    "messages",
                                ],
                            },
                        },
                    },
                    "required": ["user_info", "chats"],
                },
            )
        )

    def test_users_stats(self):
        response = self.client.get("/chats_api/users_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_users": {"type": "number"},
                    },
                    "required": ["count_users"],
                },
            },
        )

    def test_chats_stats(self):
        response = self.client.get("/chats_api/chats_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_chats": {"type": "number"},
                    },
                    "required": ["count_chats"],
                },
            },
        )

    def test_messages_stats(self):
        response = self.client.get("/chats_api/messages_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "chat": {"type": "number"},
                        "count_messages": {"type": "number"},
                    },
                    "required": ["chat", "count_messages"],
                },
            },
        )
