from django.test import TestCase, Client
from django.conf import settings
import jsonschema

from .models import (
    Status,
    Priority,
    Category,
    Role,
    Group,
    Project,
    User,
    Task,
    News,
    Comment,
)


class TasksApiTestCase(TestCase):
    fixtures = ["tasks.json"]
    client = Client()

    def test_statuses_count(self):
        self.assertEqual(Status.objects.count(), 4)

    def test_priorities_count(self):
        self.assertEqual(Priority.objects.count(), 4)

    def test_categories_count(self):
        self.assertEqual(Category.objects.count(), 5)

    def test_roles_count(self):
        self.assertEqual(Role.objects.count(), 4)

    def test_groups_count(self):
        self.assertEqual(Group.objects.count(), 3)

    def test_projects_count(self):
        self.assertEqual(Project.objects.count(), 5)

    def test_users_count(self):
        self.assertEqual(User.objects.count(), 10)

    def test_tasks_count(self):
        self.assertEqual(Task.objects.count(), 20)

    def test_news_count(self):
        self.assertEqual(News.objects.count(), 10)

    def test_comments_count(self):
        self.assertEqual(Comment.objects.count(), 30)

    def test_statuses_list(self):
        response = self.client.get("/tasks_api/statuses_list")
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
                            "is_close": {"type": "boolean"},
                            "description": {"type": "string"},
                        },
                        "required": ["id", "name", "is_close", "description"],
                    },
                },
            )
        )

    def test_statuses_detail(self):
        response = self.client.get("/tasks_api/statuses_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "is_close": {"type": "boolean"},
                        "description": {"type": "string"},
                    },
                    "required": ["id", "name", "is_close", "description"],
                },
            )
        )

    def test_statuses_search(self):
        response = self.client.get(
            "/tasks_api/statuses_search", query_params={"q": "New"}
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
                            "is_close": {"type": "boolean"},
                            "description": {"type": "string"},
                        },
                        "required": ["id", "name", "is_close", "description"],
                    },
                },
            )
        )

    def test_statuses_create(self):
        response = self.client.post(
            "/tasks_api/statuses_create",
            {"name": "Test", "is_close": False, "description": "Test status"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_statuses_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/statuses_create",
            {"name": "Test", "is_close": False},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_statuses_update(self):
        response = self.client.put(
            "/tasks_api/statuses_update/1",
            {"name": "Updated", "is_close": True, "description": "Updated desc"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_statuses_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/statuses_update/1",
            {"name": "Updated", "is_close": True, "description": "Updated desc"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_statuses_partial_update(self):
        response = self.client.patch(
            "/tasks_api/statuses_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_statuses_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/statuses_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_statuses_filter(self):
        response = self.client.get("/tasks_api/statuses_filter", query_params={"id": 1})
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
                            "is_close": {"type": "boolean"},
                            "description": {"type": "string"},
                        },
                        "required": ["id", "name", "is_close", "description"],
                    },
                },
            )
        )

    def test_statuses_delete(self):
        response = self.client.delete(
            "/tasks_api/statuses_delete/4",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_statuses_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/statuses_delete/4",
        )
        self.assertEqual(response.status_code, 403)

    def test_priorities_list(self):
        response = self.client.get("/tasks_api/priorities_list")
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
                            "active": {"type": "boolean"},
                        },
                        "required": ["id", "name", "active"],
                    },
                },
            )
        )

    def test_priorities_detail(self):
        response = self.client.get("/tasks_api/priorities_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "active": {"type": "boolean"},
                    },
                    "required": ["id", "name", "active"],
                },
            )
        )

    def test_priorities_search(self):
        response = self.client.get(
            "/tasks_api/priorities_search", query_params={"q": "Low"}
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
                            "active": {"type": "boolean"},
                        },
                        "required": ["id", "name", "active"],
                    },
                },
            )
        )

    def test_priorities_create(self):
        response = self.client.post(
            "/tasks_api/priorities_create",
            {"name": "Urgent", "active": True},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_priorities_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/priorities_create",
            {"name": "Urgent", "active": True},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_priorities_update(self):
        response = self.client.put(
            "/tasks_api/priorities_update/1",
            {"name": "Updated", "active": False},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_priorities_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/priorities_update/1",
            {"name": "Updated", "active": False},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_priorities_partial_update(self):
        response = self.client.patch(
            "/tasks_api/priorities_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_priorities_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/priorities_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_priorities_filter(self):
        response = self.client.get(
            "/tasks_api/priorities_filter", query_params={"id": 1}
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
                            "active": {"type": "boolean"},
                        },
                        "required": ["id", "name", "active"],
                    },
                },
            )
        )

    def test_priorities_delete(self):
        response = self.client.delete(
            "/tasks_api/priorities_delete/4",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_priorities_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/priorities_delete/4",
        )
        self.assertEqual(response.status_code, 403)

    def test_categories_list(self):
        response = self.client.get("/tasks_api/categories_list")
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_categories_detail(self):
        response = self.client.get("/tasks_api/categories_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                    },
                    "required": ["id", "name"],
                },
            )
        )

    def test_categories_search(self):
        response = self.client.get(
            "/tasks_api/categories_search", query_params={"q": "Category"}
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
                            "name": {"type": "string"},
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_categories_create(self):
        response = self.client.post(
            "/tasks_api/categories_create",
            {"name": "New Category"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_categories_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/categories_create",
            {"name": "New Category"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_categories_update(self):
        response = self.client.put(
            "/tasks_api/categories_update/1",
            {"name": "Updated"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_categories_filter(self):
        response = self.client.get(
            "/tasks_api/categories_filter", query_params={"id": 1}
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_categories_delete(self):
        response = self.client.delete(
            "/tasks_api/categories_delete/5",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_categories_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/categories_delete/5",
        )
        self.assertEqual(response.status_code, 403)

    def test_categories_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/categories_update/1",
            {"name": "Updated"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_categories_partial_update(self):
        response = self.client.patch(
            "/tasks_api/categories_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_categories_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/categories_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_roles_list(self):
        response = self.client.get("/tasks_api/roles_list")
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_roles_detail(self):
        response = self.client.get("/tasks_api/roles_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                    },
                    "required": ["id", "name"],
                },
            )
        )

    def test_roles_search(self):
        response = self.client.get(
            "/tasks_api/roles_search", query_params={"q": "Admin"}
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_roles_create(self):
        response = self.client.post(
            "/tasks_api/roles_create",
            {"name": "New Role"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_roles_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/roles_create",
            {"name": "New Role"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_roles_update(self):
        response = self.client.put(
            "/tasks_api/roles_update/1",
            {"name": "Updated"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_roles_filter(self):
        response = self.client.get("/tasks_api/roles_filter", query_params={"id": 1})
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_roles_delete(self):
        response = self.client.delete(
            "/tasks_api/roles_delete/4",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_roles_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/roles_delete/4",
        )
        self.assertEqual(response.status_code, 403)

    def test_roles_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/roles_update/1",
            {"name": "Updated"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_roles_partial_update(self):
        response = self.client.patch(
            "/tasks_api/roles_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_roles_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/roles_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_groups_list(self):
        response = self.client.get("/tasks_api/groups_list")
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_groups_detail(self):
        response = self.client.get("/tasks_api/groups_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                    },
                    "required": ["id", "name"],
                },
            )
        )

    def test_groups_search(self):
        response = self.client.get(
            "/tasks_api/groups_search", query_params={"q": "Alpha"}
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_groups_create(self):
        response = self.client.post(
            "/tasks_api/groups_create",
            {"name": "New Group"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_groups_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/groups_create",
            {"name": "New Group"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_groups_update(self):
        response = self.client.put(
            "/tasks_api/groups_update/1",
            {"name": "Updated"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_groups_filter(self):
        response = self.client.get("/tasks_api/groups_filter", query_params={"id": 1})
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
                        },
                        "required": ["id", "name"],
                    },
                },
            )
        )

    def test_groups_delete(self):
        response = self.client.delete(
            "/tasks_api/groups_delete/3",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_groups_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/groups_delete/3",
        )
        self.assertEqual(response.status_code, 403)

    def test_groups_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/groups_update/1",
            {"name": "Updated"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_groups_partial_update(self):
        response = self.client.patch(
            "/tasks_api/groups_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_groups_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/groups_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_projects_list(self):
        response = self.client.get("/tasks_api/projects_list")
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
                            "identifier": {"type": "string"},
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "is_public": {"type": "boolean"},
                            "parent": {"type": ["number", "null"]},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "identifier",
                            "name",
                            "description",
                            "is_public",
                            "parent",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_projects_detail(self):
        response = self.client.get("/tasks_api/projects_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "identifier": {"type": "string"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "is_public": {"type": "boolean"},
                        "parent": {"type": ["number", "null"]},
                        "created_on": {"type": "string"},
                        "updated_on": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "identifier",
                        "name",
                        "description",
                        "is_public",
                        "parent",
                        "created_on",
                        "updated_on",
                    ],
                },
            )
        )

    def test_projects_search(self):
        response = self.client.get(
            "/tasks_api/projects_search", query_params={"q": "Project"}
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
                            "identifier": {"type": "string"},
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "is_public": {"type": "boolean"},
                            "parent": {"type": ["number", "null"]},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "identifier",
                            "name",
                            "description",
                            "is_public",
                            "parent",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_projects_create(self):
        response = self.client.post(
            "/tasks_api/projects_create",
            {
                "identifier": "PRJ-TEST",
                "name": "Test Project",
                "description": "Test",
                "is_public": True,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_projects_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/projects_create",
            {
                "identifier": "PRJ-TEST",
                "name": "Test Project",
                "description": "Test",
                "is_public": True,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_projects_update(self):
        response = self.client.put(
            "/tasks_api/projects_update/1",
            {
                "identifier": "PRJ-UPD",
                "name": "Updated",
                "description": "UPD",
                "is_public": False,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_projects_filter(self):
        response = self.client.get("/tasks_api/projects_filter", query_params={"id": 1})
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
                            "identifier": {"type": "string"},
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "is_public": {"type": "boolean"},
                            "parent": {"type": ["number", "null"]},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "identifier",
                            "name",
                            "description",
                            "is_public",
                            "parent",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_projects_delete(self):
        response = self.client.delete(
            "/tasks_api/projects_delete/5",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_projects_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/projects_delete/5",
        )
        self.assertEqual(response.status_code, 403)

    def test_projects_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/projects_update/1",
            {
                "identifier": "PRJ-UPD",
                "name": "Updated",
                "description": "UPD",
                "is_public": False,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_projects_partial_update(self):
        response = self.client.patch(
            "/tasks_api/projects_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_projects_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/projects_partial_update/1",
            {"name": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_users_list(self):
        response = self.client.get("/tasks_api/tasks_users_list")
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
                            "login": {"type": "string"},
                            "admin": {"type": "boolean"},
                            "firstname": {"type": "string"},
                            "lastname": {"type": "string"},
                            "mail": {"type": "string"},
                            "role": {"type": "number"},
                            "group": {"type": "number"},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "login",
                            "admin",
                            "firstname",
                            "lastname",
                            "mail",
                            "role",
                            "group",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_tasks_users_detail(self):
        response = self.client.get("/tasks_api/tasks_users_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "login": {"type": "string"},
                        "admin": {"type": "boolean"},
                        "firstname": {"type": "string"},
                        "lastname": {"type": "string"},
                        "mail": {"type": "string"},
                        "role": {"type": "number"},
                        "group": {"type": "number"},
                        "created_on": {"type": "string"},
                        "updated_on": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "login",
                        "admin",
                        "firstname",
                        "lastname",
                        "mail",
                        "role",
                        "group",
                        "created_on",
                        "updated_on",
                    ],
                },
            )
        )

    def test_tasks_users_search(self):
        response = self.client.get(
            "/tasks_api/tasks_users_search", query_params={"q": "user"}
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
                            "login": {"type": "string"},
                            "admin": {"type": "boolean"},
                            "firstname": {"type": "string"},
                            "lastname": {"type": "string"},
                            "mail": {"type": "string"},
                            "role": {"type": "number"},
                            "group": {"type": "number"},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "login",
                            "admin",
                            "firstname",
                            "lastname",
                            "mail",
                            "role",
                            "group",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_tasks_users_create(self):
        response = self.client.post(
            "/tasks_api/tasks_users_create",
            {
                "login": "newuser",
                "admin": False,
                "firstname": "New",
                "lastname": "User",
                "mail": "new@example.com",
                "role": 1,
                "group": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_tasks_users_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/tasks_users_create",
            {
                "login": "newuser",
                "admin": False,
                "firstname": "New",
                "lastname": "User",
                "mail": "new@example.com",
                "role": 1,
                "group": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_users_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/tasks_users_update/1",
            {
                "login": "updated",
                "admin": True,
                "firstname": "Upd",
                "lastname": "User",
                "mail": "upd@example.com",
                "role": 1,
                "group": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_users_update(self):
        response = self.client.put(
            "/tasks_api/tasks_users_update/1",
            {
                "login": "updated",
                "admin": True,
                "firstname": "Upd",
                "lastname": "User",
                "mail": "upd@example.com",
                "role": 1,
                "group": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_tasks_users_partial_update(self):
        response = self.client.patch(
            "/tasks_api/tasks_users_partial_update/1",
            {"login": "patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_tasks_users_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/tasks_users_partial_update/1",
            {"login": "patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_users_filter(self):
        response = self.client.get(
            "/tasks_api/tasks_users_filter", query_params={"id": 1}
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
                            "login": {"type": "string"},
                            "admin": {"type": "boolean"},
                            "firstname": {"type": "string"},
                            "lastname": {"type": "string"},
                            "mail": {"type": "string"},
                            "role": {"type": "number"},
                            "group": {"type": "number"},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "login",
                            "admin",
                            "firstname",
                            "lastname",
                            "mail",
                            "role",
                            "group",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_tasks_users_delete(self):
        response = self.client.delete(
            "/tasks_api/tasks_users_delete/10",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_tasks_users_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/tasks_users_delete/10",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_list(self):
        response = self.client.get("/tasks_api/tasks_list")
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
                            "subject": {"type": "string"},
                            "description": {"type": "string"},
                            "start_date": {"type": "string"},
                            "due_date": {"type": ["string", "null"]},
                            "is_private": {"type": "boolean"},
                            "done_percent": {"type": "number"},
                            "closed_on": {"type": ["string", "null"]},
                            "spent_days": {"type": ["number", "null"]},
                            "estimated_days": {"type": ["number", "null"]},
                            "parent": {"type": ["number", "null"]},
                            "category": {"type": "number"},
                            "assigned_to": {"type": "number"},
                            "author": {"type": "number"},
                            "priority": {"type": "number"},
                            "status": {"type": "number"},
                            "project": {"type": "number"},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "subject",
                            "description",
                            "start_date",
                            "due_date",
                            "is_private",
                            "done_percent",
                            "closed_on",
                            "spent_days",
                            "estimated_days",
                            "parent",
                            "category",
                            "assigned_to",
                            "author",
                            "priority",
                            "status",
                            "project",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_tasks_detail(self):
        response = self.client.get("/tasks_api/tasks_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "start_date": {"type": "string"},
                        "due_date": {"type": ["string", "null"]},
                        "is_private": {"type": "boolean"},
                        "done_percent": {"type": "number"},
                        "closed_on": {"type": ["string", "null"]},
                        "spent_days": {"type": ["number", "null"]},
                        "estimated_days": {"type": ["number", "null"]},
                        "parent": {"type": ["number", "null"]},
                        "category": {"type": "number"},
                        "assigned_to": {"type": "number"},
                        "author": {"type": "number"},
                        "priority": {"type": "number"},
                        "status": {"type": "number"},
                        "project": {"type": "number"},
                        "created_on": {"type": "string"},
                        "updated_on": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "subject",
                        "description",
                        "start_date",
                        "due_date",
                        "is_private",
                        "done_percent",
                        "closed_on",
                        "spent_days",
                        "estimated_days",
                        "parent",
                        "category",
                        "assigned_to",
                        "author",
                        "priority",
                        "status",
                        "project",
                        "created_on",
                        "updated_on",
                    ],
                },
            )
        )

    def test_tasks_search(self):
        response = self.client.get(
            "/tasks_api/tasks_search", query_params={"q": "Task"}
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
                            "subject": {"type": "string"},
                            "description": {"type": "string"},
                            "start_date": {"type": "string"},
                            "due_date": {"type": ["string", "null"]},
                            "is_private": {"type": "boolean"},
                            "done_percent": {"type": "number"},
                            "closed_on": {"type": ["string", "null"]},
                            "spent_days": {"type": ["number", "null"]},
                            "estimated_days": {"type": ["number", "null"]},
                            "parent": {"type": ["number", "null"]},
                            "category": {"type": "number"},
                            "assigned_to": {"type": "number"},
                            "author": {"type": "number"},
                            "priority": {"type": "number"},
                            "status": {"type": "number"},
                            "project": {"type": "number"},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "subject",
                            "description",
                            "start_date",
                            "due_date",
                            "is_private",
                            "done_percent",
                            "closed_on",
                            "spent_days",
                            "estimated_days",
                            "parent",
                            "category",
                            "assigned_to",
                            "author",
                            "priority",
                            "status",
                            "project",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_tasks_create(self):
        response = self.client.post(
            "/tasks_api/tasks_create",
            {
                "subject": "New Task",
                "description": "Desc",
                "start_date": "2025-06-01",
                "is_private": False,
                "done_percent": 0,
                "category": 1,
                "assigned_to": 1,
                "author": 1,
                "priority": 1,
                "status": 1,
                "project": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_tasks_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/tasks_create",
            {
                "subject": "New Task",
                "description": "Desc",
                "start_date": "2025-06-01",
                "is_private": False,
                "done_percent": 0,
                "category": 1,
                "assigned_to": 1,
                "author": 1,
                "priority": 1,
                "status": 1,
                "project": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/tasks_update/1",
            {
                "subject": "Updated",
                "description": "Desc",
                "start_date": "2025-06-01",
                "is_private": True,
                "done_percent": 50,
                "category": 1,
                "assigned_to": 1,
                "author": 1,
                "priority": 1,
                "status": 1,
                "project": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_update(self):
        response = self.client.put(
            "/tasks_api/tasks_update/1",
            {
                "subject": "Updated",
                "description": "Desc",
                "start_date": "2025-06-01",
                "is_private": True,
                "done_percent": 50,
                "category": 1,
                "assigned_to": 1,
                "author": 1,
                "priority": 1,
                "status": 1,
                "project": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_tasks_partial_update(self):
        response = self.client.patch(
            "/tasks_api/tasks_partial_update/1",
            {"subject": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_tasks_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/tasks_partial_update/1",
            {"subject": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_tasks_filter(self):
        response = self.client.get(
            "/tasks_api/tasks_filter", query_params={"project": 1}
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
                            "subject": {"type": "string"},
                            "description": {"type": "string"},
                            "start_date": {"type": "string"},
                            "due_date": {"type": ["string", "null"]},
                            "is_private": {"type": "boolean"},
                            "done_percent": {"type": "number"},
                            "closed_on": {"type": ["string", "null"]},
                            "spent_days": {"type": ["number", "null"]},
                            "estimated_days": {"type": ["number", "null"]},
                            "parent": {"type": ["number", "null"]},
                            "category": {"type": "number"},
                            "assigned_to": {"type": "number"},
                            "author": {"type": "number"},
                            "priority": {"type": "number"},
                            "status": {"type": "number"},
                            "project": {"type": "number"},
                            "created_on": {"type": "string"},
                            "updated_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "subject",
                            "description",
                            "start_date",
                            "due_date",
                            "is_private",
                            "done_percent",
                            "closed_on",
                            "spent_days",
                            "estimated_days",
                            "parent",
                            "category",
                            "assigned_to",
                            "author",
                            "priority",
                            "status",
                            "project",
                            "created_on",
                            "updated_on",
                        ],
                    },
                },
            )
        )

    def test_tasks_delete(self):
        response = self.client.delete(
            "/tasks_api/tasks_delete/20",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_tasks_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/tasks_delete/20",
        )
        self.assertEqual(response.status_code, 403)

    def test_news_list(self):
        response = self.client.get("/tasks_api/news_list")
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
                            "summary": {"type": "string"},
                            "description": {"type": "string"},
                            "project": {"type": "number"},
                            "author": {"type": "number"},
                            "created_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "title",
                            "summary",
                            "description",
                            "project",
                            "author",
                            "created_on",
                        ],
                    },
                },
            )
        )

    def test_news_detail(self):
        response = self.client.get("/tasks_api/news_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "summary": {"type": "string"},
                        "description": {"type": "string"},
                        "project": {"type": "number"},
                        "author": {"type": "number"},
                        "created_on": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "title",
                        "summary",
                        "description",
                        "project",
                        "author",
                        "created_on",
                    ],
                },
            )
        )

    def test_news_search(self):
        response = self.client.get("/tasks_api/news_search", query_params={"q": "News"})
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
                            "summary": {"type": "string"},
                            "description": {"type": "string"},
                            "project": {"type": "number"},
                            "author": {"type": "number"},
                            "created_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "title",
                            "summary",
                            "description",
                            "project",
                            "author",
                            "created_on",
                        ],
                    },
                },
            )
        )

    def test_news_create(self):
        response = self.client.post(
            "/tasks_api/news_create",
            {
                "title": "New News",
                "summary": "Sum",
                "description": "Desc",
                "project": 1,
                "author": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_news_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/news_create",
            {
                "title": "New News",
                "summary": "Sum",
                "description": "Desc",
                "project": 1,
                "author": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_news_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/news_update/1",
            {
                "title": "Updated",
                "summary": "Sum",
                "description": "Desc",
                "project": 1,
                "author": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_news_update(self):
        response = self.client.put(
            "/tasks_api/news_update/1",
            {
                "title": "Updated",
                "summary": "Sum",
                "description": "Desc",
                "project": 1,
                "author": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_news_partial_update(self):
        response = self.client.patch(
            "/tasks_api/news_partial_update/1",
            {"title": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_news_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/news_partial_update/1",
            {"title": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_news_filter(self):
        response = self.client.get(
            "/tasks_api/news_filter", query_params={"project": 1}
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
                            "summary": {"type": "string"},
                            "description": {"type": "string"},
                            "project": {"type": "number"},
                            "author": {"type": "number"},
                            "created_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "title",
                            "summary",
                            "description",
                            "project",
                            "author",
                            "created_on",
                        ],
                    },
                },
            )
        )

    def test_news_delete(self):
        response = self.client.delete(
            "/tasks_api/news_delete/10",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_news_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/news_delete/10",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_list(self):
        response = self.client.get("/tasks_api/comments_list")
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
                            "content": {"type": "string"},
                            "author": {"type": "number"},
                            "some_news": {"type": "number"},
                            "created_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "content",
                            "author",
                            "some_news",
                            "created_on",
                        ],
                    },
                },
            )
        )

    def test_comments_detail(self):
        response = self.client.get("/tasks_api/comments_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "content": {"type": "string"},
                        "author": {"type": "number"},
                        "some_news": {"type": "number"},
                        "created_on": {"type": "string"},
                    },
                    "required": ["id", "content", "author", "some_news", "created_on"],
                },
            )
        )

    def test_comments_search(self):
        response = self.client.get(
            "/tasks_api/comments_search", query_params={"q": "Comment"}
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
                            "content": {"type": "string"},
                            "author": {"type": "number"},
                            "some_news": {"type": "number"},
                            "created_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "content",
                            "author",
                            "some_news",
                            "created_on",
                        ],
                    },
                },
            )
        )

    def test_comments_create(self):
        response = self.client.post(
            "/tasks_api/comments_create",
            {"content": "New comment", "author": 1, "some_news": 1},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_comments_create_forbidden(self):
        response = self.client.post(
            "/tasks_api/comments_create",
            {"content": "New comment", "author": 1, "some_news": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_update_forbidden(self):
        response = self.client.put(
            "/tasks_api/comments_update/1",
            {"content": "Updated", "author": 1, "some_news": 1},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_update(self):
        response = self.client.put(
            "/tasks_api/comments_update/1",
            {"content": "Updated", "author": 1, "some_news": 1},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_comments_partial_update(self):
        response = self.client.patch(
            "/tasks_api/comments_partial_update/1",
            {"content": "Patched"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_comments_partial_update_forbidden(self):
        response = self.client.patch(
            "/tasks_api/comments_partial_update/1",
            {"content": "Patched"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_filter(self):
        response = self.client.get(
            "/tasks_api/comments_filter", query_params={"author": 1}
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
                            "content": {"type": "string"},
                            "author": {"type": "number"},
                            "some_news": {"type": "number"},
                            "created_on": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "content",
                            "author",
                            "some_news",
                            "created_on",
                        ],
                    },
                },
            )
        )

    def test_comments_delete(self):
        response = self.client.delete(
            "/tasks_api/comments_delete/30",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_comments_delete_forbidden(self):
        response = self.client.delete(
            "/tasks_api/comments_delete/30",
        )
        self.assertEqual(response.status_code, 403)

    def test_profile(self):
        response = self.client.get("/tasks_api/profile/1")
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
                                "login": {"type": "string"},
                                "firstname": {"type": "string"},
                                "lastname": {"type": "string"},
                                "mail": {"type": "string"},
                                "admin": {"type": "boolean"},
                            },
                            "required": [
                                "login",
                                "firstname",
                                "lastname",
                                "mail",
                                "admin",
                            ],
                        },
                        "tasks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "number"},
                                    "subject": {"type": "string"},
                                    "description": {"type": "string"},
                                    "done_percent": {"type": "number"},
                                },
                                "required": [
                                    "id",
                                    "subject",
                                    "description",
                                    "done_percent",
                                ],
                            },
                        },
                        "news": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "number"},
                                    "title": {"type": "string"},
                                    "summary": {"type": "string"},
                                },
                                "required": ["id", "title", "summary"],
                            },
                        },
                        "comments": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "number"},
                                    "content": {"type": "string"},
                                    "created_on": {"type": "string"},
                                },
                                "required": ["id", "content", "created_on"],
                            },
                        },
                    },
                    "required": ["user_info", "tasks", "news", "comments"],
                },
            )
        )

    def test_statuses_stats(self):
        response = self.client.get("/tasks_api/statuses_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_statuses": {"type": "number"},
                    },
                    "required": ["count_statuses"],
                },
            },
        )

    def test_priorities_stats(self):
        response = self.client.get("/tasks_api/priorities_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_priorities": {"type": "number"},
                    },
                    "required": ["count_priorities"],
                },
            },
        )

    def test_categories_stats(self):
        response = self.client.get("/tasks_api/categories_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_categories": {"type": "number"},
                    },
                    "required": ["count_categories"],
                },
            },
        )

    def test_roles_stats(self):
        response = self.client.get("/tasks_api/roles_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_roles": {"type": "number"},
                    },
                    "required": ["count_roles"],
                },
            },
        )

    def test_groups_stats(self):
        response = self.client.get("/tasks_api/groups_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_groups": {"type": "number"},
                    },
                    "required": ["count_groups"],
                },
            },
        )

    def test_projects_stats(self):
        response = self.client.get("/tasks_api/projects_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count_projects": {"type": "number"},
                    },
                    "required": ["count_projects"],
                },
            },
        )

    def test_tasks_users_stats(self):
        response = self.client.get("/tasks_api/tasks_users_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "role": {"type": "number"},
                        "count_users": {"type": "number"},
                    },
                    "required": ["role", "count_users"],
                },
            },
        )

    def test_tasks_stats(self):
        response = self.client.get("/tasks_api/tasks_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "project": {"type": "number"},
                        "count_tasks": {"type": "number"},
                    },
                    "required": ["project", "count_tasks"],
                },
            },
        )

    def test_news_stats(self):
        response = self.client.get("/tasks_api/news_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "project": {"type": "number"},
                        "count_news": {"type": "number"},
                    },
                    "required": ["project", "count_news"],
                },
            },
        )

    def test_comments_stats(self):
        response = self.client.get("/tasks_api/comments_stats")
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(
            response.json(),
            {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "some_news": {"type": "number"},
                        "count_comments": {"type": "number"},
                    },
                    "required": ["some_news", "count_comments"],
                },
            },
        )
