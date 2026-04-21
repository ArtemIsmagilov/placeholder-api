from django.test import TestCase, Client
from django.conf import settings
import jsonschema

from dummy_api.models import (
    User,
    Todo,
    Recipe,
    Quote,
    Product,
    Review,
    Post,
    Comment,
    Cart,
)


class DummyApiTestCase(TestCase):
    fixtures = ["d.json"]
    client = Client()

    def test_users(self):
        self.assertEqual(User.objects.count(), 208)

    def test_todos(self):
        self.assertEqual(Todo.objects.count(), 254)

    def test_recipes(self):
        self.assertEqual(Recipe.objects.count(), 50)

    def test_quotes(self):
        self.assertEqual(Quote.objects.count(), 1454)

    def test_products(self):
        self.assertEqual(Product.objects.count(), 194)

    def test_reviews(self):
        self.assertEqual(Review.objects.count(), 582)

    def test_posts(self):
        self.assertEqual(Post.objects.count(), 251)

    def test_comments(self):
        self.assertEqual(Comment.objects.count(), 340)

    def test_carts(self):
        self.assertEqual(Cart.objects.count(), 208)

    def test_users_list(self):
        response = self.client.get("/dummy_api/users_list")
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
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "maiden_name": {"type": "string"},
                            "age": {"type": "number"},
                            "gender": {"type": "string"},
                            "email": {"type": "string"},
                            "phone": {"type": "string"},
                            "username": {"type": "string"},
                            "password": {"type": "string"},
                            "birthday": {"type": "string"},
                            "image": {"type": "string"},
                            "blood_group": {"type": "string"},
                            "height": {"type": "number"},
                            "weight": {"type": "number"},
                            "eye_color": {"type": "string"},
                            "hair_color": {"type": "string"},
                            "hair_type": {"type": "string"},
                            "ip": {"type": "string"},
                            "address": {"type": "string"},
                            "city": {"type": "string"},
                            "state": {"type": "string"},
                            "state_code": {"type": "string"},
                            "postal_code": {"type": "string"},
                            "coordinates": {"type": "string"},
                            "country": {"type": "string"},
                            "mac_address": {"type": "string"},
                            "university": {"type": "string"},
                            "bank_card_expire": {"type": "string"},
                            "bank_card_number": {"type": "string"},
                            "bank_card_type": {"type": "string"},
                            "bank_currency": {"type": "string"},
                            "bank_iban": {"type": "string"},
                            "company_department": {"type": "string"},
                            "company_name": {"type": "string"},
                            "company_title": {"type": "string"},
                            "company_address": {"type": "string"},
                            "company_city": {"type": "string"},
                            "company_state": {"type": "string"},
                            "company_state_code": {"type": "string"},
                            "company_postal_code": {"type": "string"},
                            "company_coordinates": {"type": "string"},
                            "company_country": {"type": "string"},
                            "ein": {"type": "string"},
                            "snn": {"type": "string"},
                            "user_agent": {"type": "string"},
                            "crypto_coint": {"type": "string"},
                            "crypto_wallet": {"type": "string"},
                            "crypto_network": {"type": "string"},
                            "role": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "first_name",
                            "last_name",
                            "maiden_name",
                            "age",
                            "gender",
                            "email",
                            "phone",
                            "username",
                            "password",
                            "birthday",
                            "image",
                            "blood_group",
                            "height",
                            "weight",
                            "eye_color",
                            "hair_color",
                            "hair_type",
                            "ip",
                            "address",
                            "city",
                            "state",
                            "state_code",
                            "postal_code",
                            "coordinates",
                            "country",
                            "mac_address",
                            "university",
                            "bank_card_expire",
                            "bank_card_number",
                            "bank_card_type",
                            "bank_currency",
                            "bank_iban",
                            "company_department",
                            "company_name",
                            "company_title",
                            "company_address",
                            "company_city",
                            "company_state",
                            "company_state_code",
                            "company_postal_code",
                            "company_coordinates",
                            "company_country",
                            "ein",
                            "snn",
                            "user_agent",
                            "crypto_coint",
                            "crypto_wallet",
                            "crypto_network",
                            "role",
                        ],
                    },
                },
            )
        )

    def test_users_detail(self):
        response = self.client.get("/dummy_api/users_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "maiden_name": {"type": "string"},
                        "age": {"type": "number"},
                        "gender": {"type": "string"},
                        "email": {"type": "string"},
                        "phone": {"type": "string"},
                        "username": {"type": "string"},
                        "password": {"type": "string"},
                        "birthday": {"type": "string"},
                        "image": {"type": "string"},
                        "blood_group": {"type": "string"},
                        "height": {"type": "number"},
                        "weight": {"type": "number"},
                        "eye_color": {"type": "string"},
                        "hair_color": {"type": "string"},
                        "hair_type": {"type": "string"},
                        "ip": {"type": "string"},
                        "address": {"type": "string"},
                        "city": {"type": "string"},
                        "state": {"type": "string"},
                        "state_code": {"type": "string"},
                        "postal_code": {"type": "string"},
                        "coordinates": {"type": "string"},
                        "country": {"type": "string"},
                        "mac_address": {"type": "string"},
                        "university": {"type": "string"},
                        "bank_card_expire": {"type": "string"},
                        "bank_card_number": {"type": "string"},
                        "bank_card_type": {"type": "string"},
                        "bank_currency": {"type": "string"},
                        "bank_iban": {"type": "string"},
                        "company_department": {"type": "string"},
                        "company_name": {"type": "string"},
                        "company_title": {"type": "string"},
                        "company_address": {"type": "string"},
                        "company_city": {"type": "string"},
                        "company_state": {"type": "string"},
                        "company_state_code": {"type": "string"},
                        "company_postal_code": {"type": "string"},
                        "company_coordinates": {"type": "string"},
                        "company_country": {"type": "string"},
                        "ein": {"type": "string"},
                        "snn": {"type": "string"},
                        "user_agent": {"type": "string"},
                        "crypto_coint": {"type": "string"},
                        "crypto_wallet": {"type": "string"},
                        "crypto_network": {"type": "string"},
                        "role": {"type": "string"},
                    },
                    "required": [
                        "id", "first_name", "last_name", "maiden_name", "age", "gender", "email",
                        "phone", "username", "password", "birthday", "image", "blood_group",
                        "height", "weight", "eye_color", "hair_color", "hair_type", "ip",
                        "address", "city", "state", "state_code", "postal_code", "coordinates",
                        "country", "mac_address", "university", "bank_card_expire", "bank_card_number",
                        "bank_card_type", "bank_currency", "bank_iban", "company_department",
                        "company_name", "company_title", "company_address", "company_city",
                        "company_state", "company_state_code", "company_postal_code",
                        "company_coordinates", "company_country", "ein", "snn", "user_agent",
                        "crypto_coint", "crypto_wallet", "crypto_network", "role",
                    ],
                },
            )
        )

    def test_users_create(self):
        response = self.client.post(
            "/dummy_api/users_create",
            {
                "first_name": "John",
                "last_name": "Doe",
                "maiden_name": "Smith",
                "age": 25,
                "gender": "male",
                "email": "john@example.com",
                "phone": "+1234567890",
                "username": "johnd",
                "password": "password123",
                "birthday": "1999-01-01",
                "image": "https://example.com/image.jpg",
                "blood_group": "O+",
                "height": 180.0,
                "weight": 75.0,
                "eye_color": "blue",
                "hair_color": "brown",
                "hair_type": "curly",
                "ip": "192.168.1.1",
                "address": "123 Main St",
                "city": "New York",
                "state": "NY",
                "state_code": "NY",
                "postal_code": "10001",
                "coordinates": "40.7128 -74.0060",
                "country": "USA",
                "mac_address": "00:11:22:33:44:55",
                "university": "Harvard",
                "bank_card_expire": "12/25",
                "bank_card_number": "4111111111111111",
                "bank_card_type": "Visa",
                "bank_currency": "USD",
                "bank_iban": "GB82WEST12345698765432",
                "company_department": "Engineering",
                "company_name": "Acme Inc",
                "company_title": "Developer",
                "company_address": "456 Corporate Blvd",
                "company_city": "San Francisco",
                "company_state": "CA",
                "company_state_code": "CA",
                "company_postal_code": "94105",
                "company_coordinates": "37.7749 -122.4194",
                "company_country": "USA",
                "ein": "12-3456789",
                "snn": "123-45-6789",
                "user_agent": "Mozilla/5.0",
                "crypto_coint": "Bitcoin",
                "crypto_wallet": "0x1234567890abcdef",
                "crypto_network": "Ethereum",
                "role": "user",
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_users_update(self):
        response = self.client.put(
            "/dummy_api/users_update/1",
            {
                "first_name": "John Updated",
                "last_name": "Doe",
                "maiden_name": "Smith",
                "age": 25,
                "gender": "male",
                "email": "john@example.com",
                "phone": "+1234567890",
                "username": "johnd",
                "password": "password123",
                "birthday": "1999-01-01",
                "image": "https://example.com/image.jpg",
                "blood_group": "O+",
                "height": 180.0,
                "weight": 75.0,
                "eye_color": "blue",
                "hair_color": "brown",
                "hair_type": "curly",
                "ip": "192.168.1.1",
                "address": "123 Main St",
                "city": "New York",
                "state": "NY",
                "state_code": "NY",
                "postal_code": "10001",
                "coordinates": "40.7128 -74.0060",
                "country": "USA",
                "mac_address": "00:11:22:33:44:55",
                "university": "Harvard",
                "bank_card_expire": "12/25",
                "bank_card_number": "4111111111111111",
                "bank_card_type": "Visa",
                "bank_currency": "USD",
                "bank_iban": "GB82WEST12345698765432",
                "company_department": "Engineering",
                "company_name": "Acme Inc",
                "company_title": "Developer",
                "company_address": "456 Corporate Blvd",
                "company_city": "San Francisco",
                "company_state": "CA",
                "company_state_code": "CA",
                "company_postal_code": "94105",
                "company_coordinates": "37.7749 -122.4194",
                "company_country": "USA",
                "ein": "12-3456789",
                "snn": "123-45-6789",
                "user_agent": "Mozilla/5.0",
                "crypto_coint": "Bitcoin",
                "crypto_wallet": "0x1234567890abcdef",
                "crypto_network": "Ethereum",
                "role": "user",
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_users_partial_update(self):
        response = self.client.patch(
            "/dummy_api/users_partial_update/1",
            {"first_name": "Jane"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_users_filter(self):
        response = self.client.get("/dummy_api/users_filter", {"first_name": "Emily"})
        self.assertEqual(response.status_code, 200)

    def test_users_delete(self):
        response = self.client.delete(
            "/dummy_api/users_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_todos_list(self):
        response = self.client.get("/dummy_api/todos_list")
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
        response = self.client.get("/dummy_api/todos_detail/1")
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

    def test_todos_create(self):
        response = self.client.post(
            "/dummy_api/todos_create",
            {
                "title": "New Todo",
                "completed": False,
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_todos_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/todos_create",
            {
                "title": "New Todo",
                "completed": False,
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_todos_update(self):
        response = self.client.put(
            "/dummy_api/todos_update/1",
            {
                "title": "Updated Todo",
                "completed": True,
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_todos_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/todos_update/1",
            {
                "title": "Updated Todo",
                "completed": True,
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_todos_partial_update(self):
        response = self.client.patch(
            "/dummy_api/todos_partial_update/1",
            {"completed": True},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_todos_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/todos_partial_update/1",
            {"completed": True},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_todos_filter(self):
        response = self.client.get("/dummy_api/todos_filter", {"completed": True})
        self.assertEqual(response.status_code, 200)

    def test_todos_delete(self):
        response = self.client.delete(
            "/dummy_api/todos_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_todos_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/todos_delete/1",
        )
        self.assertEqual(response.status_code, 403)

    def test_recipes_list(self):
        response = self.client.get("/dummy_api/recipes_list")
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
                            "ingredients": {"type": "string"},
                            "instructions": {"type": "string"},
                            "prep_time_minutes": {"type": "number"},
                            "cook_time_minutes": {"type": "number"},
                            "servings": {"type": "number"},
                            "difficulty": {"type": "string"},
                            "cuisine": {"type": "string"},
                            "calories_per_serving": {"type": "number"},
                            "tags": {"type": "string"},
                            "image": {"type": "string"},
                            "rating": {"type": "number"},
                            "review_count": {"type": "number"},
                            "meal_type": {"type": "string"},
                            "user": {"type": "number"},
                        },
                        "required": [
                            "id",
                            "name",
                            "ingredients",
                            "instructions",
                            "prep_time_minutes",
                            "cook_time_minutes",
                            "servings",
                            "difficulty",
                            "cuisine",
                            "calories_per_serving",
                            "tags",
                            "image",
                            "rating",
                            "review_count",
                            "meal_type",
                            "user",
                        ],
                    },
                },
            )
        )

    def test_recipes_detail(self):
        response = self.client.get("/dummy_api/recipes_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "ingredients": {"type": "string"},
                        "instructions": {"type": "string"},
                        "prep_time_minutes": {"type": "number"},
                        "cook_time_minutes": {"type": "number"},
                        "servings": {"type": "number"},
                        "difficulty": {"type": "string"},
                        "cuisine": {"type": "string"},
                        "calories_per_serving": {"type": "number"},
                        "tags": {"type": "string"},
                        "image": {"type": "string"},
                        "rating": {"type": "number"},
                        "review_count": {"type": "number"},
                        "meal_type": {"type": "string"},
                        "user": {"type": "number"},
                    },
                    "required": [
                        "id",
                        "name",
                        "ingredients",
                        "instructions",
                        "prep_time_minutes",
                        "cook_time_minutes",
                        "servings",
                        "difficulty",
                        "cuisine",
                        "calories_per_serving",
                        "tags",
                        "image",
                        "rating",
                        "review_count",
                        "meal_type",
                        "user",
                    ],
                },
            )
        )

    def test_recipes_create(self):
        response = self.client.post(
            "/dummy_api/recipes_create",
            {
                "name": "New Recipe",
                "ingredients": "ingredient1, ingredient2",
                "instructions": "Cook it",
                "prep_time_minutes": 10,
                "cook_time_minutes": 20,
                "servings": 4,
                "difficulty": "easy",
                "cuisine": "Italian",
                "calories_per_serving": 300,
                "tags": "pasta,italian",
                "image": "https://example.com/image.jpg",
                "rating": 4.5,
                "review_count": 100,
                "meal_type": "dinner",
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_recipes_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/recipes_create",
            {
                "name": "New Recipe",
                "ingredients": "ingredient1, ingredient2",
                "instructions": "Cook it",
                "prep_time_minutes": 10,
                "cook_time_minutes": 20,
                "servings": 4,
                "difficulty": "easy",
                "cuisine": "Italian",
                "calories_per_serving": 300,
                "tags": "pasta,italian",
                "image": "https://example.com/image.jpg",
                "rating": 4.5,
                "review_count": 100,
                "meal_type": "dinner",
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_recipes_update(self):
        response = self.client.put(
            "/dummy_api/recipes_update/1",
            {
                "name": "Updated Recipe",
                "ingredients": "ingredient1, ingredient2",
                "instructions": "Cook it",
                "prep_time_minutes": 10,
                "cook_time_minutes": 20,
                "servings": 4,
                "difficulty": "easy",
                "cuisine": "Italian",
                "calories_per_serving": 300,
                "tags": "pasta,italian",
                "image": "https://example.com/image.jpg",
                "rating": 4.5,
                "review_count": 100,
                "meal_type": "dinner",
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_recipes_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/recipes_update/1",
            {
                "name": "Updated Recipe",
                "ingredients": "ingredient1, ingredient2",
                "instructions": "Cook it",
                "prep_time_minutes": 10,
                "cook_time_minutes": 20,
                "servings": 4,
                "difficulty": "easy",
                "cuisine": "Italian",
                "calories_per_serving": 300,
                "tags": "pasta,italian",
                "image": "https://example.com/image.jpg",
                "rating": 4.5,
                "review_count": 100,
                "meal_type": "dinner",
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_recipes_partial_update(self):
        response = self.client.patch(
            "/dummy_api/recipes_partial_update/1",
            {"name": "Updated Name"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_recipes_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/recipes_partial_update/1",
            {"name": "Updated Name"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_recipes_filter(self):
        response = self.client.get("/dummy_api/recipes_filter", {"cuisine": "Italian"})
        self.assertEqual(response.status_code, 200)

    def test_recipes_delete(self):
        response = self.client.delete(
            "/dummy_api/recipes_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_recipes_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/recipes_delete/1",
        )
        self.assertEqual(response.status_code, 403)

    def test_quotes_list(self):
        response = self.client.get("/dummy_api/quotes_list")
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
                            "author": {"type": "string"},
                        },
                        "required": ["id", "title", "author"],
                    },
                },
            )
        )

    def test_quotes_detail(self):
        response = self.client.get("/dummy_api/quotes_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "author": {"type": "string"},
                    },
                    "required": ["id", "title", "author"],
                },
            )
        )

    def test_quotes_create(self):
        response = self.client.post(
            "/dummy_api/quotes_create",
            {"title": "New Quote", "author": "John Doe"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_quotes_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/quotes_create",
            {"title": "New Quote", "author": "John Doe"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_quotes_update(self):
        response = self.client.put(
            "/dummy_api/quotes_update/1",
            {"title": "Updated Quote", "author": "John Doe"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_quotes_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/quotes_update/1",
            {"title": "Updated Quote", "author": "John Doe"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_quotes_partial_update(self):
        response = self.client.patch(
            "/dummy_api/quotes_partial_update/1",
            {"title": "New Title"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_quotes_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/quotes_partial_update/1",
            {"title": "New Title"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_quotes_filter(self):
        response = self.client.get("/dummy_api/quotes_filter", {"author": "Unknown"})
        self.assertEqual(response.status_code, 200)

    def test_quotes_delete(self):
        response = self.client.delete(
            "/dummy_api/quotes_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_quotes_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/quotes_delete/1",
        )
        self.assertEqual(response.status_code, 403)

    def test_products_list(self):
        response = self.client.get("/dummy_api/products_list")
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
                            "description": {"type": "string"},
                            "category": {"type": "string"},
                            "price": {"type": "number"},
                            "discount_percentage": {"type": "number"},
                            "rating": {"type": "number"},
                            "stock": {"type": "number"},
                            "tags": {"type": "string"},
                            "brand": {"type": "string"},
                            "sku": {"type": "string"},
                            "weight": {"type": "number"},
                            "width": {"type": "number"},
                            "height": {"type": "number"},
                            "depth": {"type": "number"},
                            "warranty_information": {"type": "string"},
                            "shipping_information": {"type": "string"},
                            "availability_status": {"type": "string"},
                            "return_policy": {"type": "string"},
                            "minimum_order_quantity": {"type": "number"},
                            "created_at": {"type": "string"},
                            "updated_at": {"type": "string"},
                            "barcode": {"type": "string"},
                            "qr_code": {"type": "string"},
                            "thumbnail": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "title",
                            "description",
                            "category",
                            "price",
                            "discount_percentage",
                            "rating",
                            "stock",
                            "tags",
                            "brand",
                            "sku",
                            "weight",
                            "width",
                            "height",
                            "depth",
                            "warranty_information",
                            "shipping_information",
                            "availability_status",
                            "return_policy",
                            "minimum_order_quantity",
                            "created_at",
                            "updated_at",
                            "barcode",
                            "qr_code",
                            "thumbnail",
                        ],
                    },
                },
            )
        )

    def test_products_detail(self):
        response = self.client.get("/dummy_api/products_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "category": {"type": "string"},
                        "price": {"type": "number"},
                        "discount_percentage": {"type": "number"},
                        "rating": {"type": "number"},
                        "stock": {"type": "number"},
                        "tags": {"type": "string"},
                        "brand": {"type": "string"},
                        "sku": {"type": "string"},
                        "weight": {"type": "number"},
                        "width": {"type": "number"},
                        "height": {"type": "number"},
                        "depth": {"type": "number"},
                        "warranty_information": {"type": "string"},
                        "shipping_information": {"type": "string"},
                        "availability_status": {"type": "string"},
                        "return_policy": {"type": "string"},
                        "minimum_order_quantity": {"type": "number"},
                        "created_at": {"type": "string"},
                        "updated_at": {"type": "string"},
                        "barcode": {"type": "string"},
                        "qr_code": {"type": "string"},
                        "thumbnail": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "title",
                        "description",
                        "category",
                        "price",
                        "discount_percentage",
                        "rating",
                        "stock",
                        "tags",
                        "brand",
                        "sku",
                        "weight",
                        "width",
                        "height",
                        "depth",
                        "warranty_information",
                        "shipping_information",
                        "availability_status",
                        "return_policy",
                        "minimum_order_quantity",
                        "created_at",
                        "updated_at",
                        "barcode",
                        "qr_code",
                        "thumbnail",
                    ],
                },
            )
        )

    def test_products_create(self):
        response = self.client.post(
            "/dummy_api/products_create",
            {
                "title": "New Product",
                "description": "A great product",
                "category": "electronics",
                "price": 99.99,
                "discount_percentage": 10.0,
                "rating": 4.5,
                "stock": 100,
                "tags": "sale,new",
                "brand": "Brand",
                "sku": "SKU123",
                "weight": 1,
                "width": 10.0,
                "height": 10.0,
                "depth": 10.0,
                "warranty_information": "1 year",
                "shipping_information": "Free shipping",
                "availability_status": "In Stock",
                "return_policy": "30 days",
                "minimum_order_quantity": 1,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "barcode": "123456789",
                "qr_code": "https://example.com/qr.png",
                "thumbnail": "https://example.com/thumb.png",
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_products_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/products_create",
            {
                "title": "New Product",
                "description": "A great product",
                "category": "electronics",
                "price": 99.99,
                "discount_percentage": 10.0,
                "rating": 4.5,
                "stock": 100,
                "tags": "sale,new",
                "brand": "Brand",
                "sku": "SKU123",
                "weight": 1,
                "width": 10.0,
                "height": 10.0,
                "depth": 10.0,
                "warranty_information": "1 year",
                "shipping_information": "Free shipping",
                "availability_status": "In Stock",
                "return_policy": "30 days",
                "minimum_order_quantity": 1,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "barcode": "123456789",
                "qr_code": "https://example.com/qr.png",
                "thumbnail": "https://example.com/thumb.png",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_products_update(self):
        response = self.client.put(
            "/dummy_api/products_update/1",
            {
                "title": "Updated Product",
                "description": "A great product",
                "category": "electronics",
                "price": 99.99,
                "discount_percentage": 10.0,
                "rating": 4.5,
                "stock": 100,
                "tags": "sale,new",
                "brand": "Brand",
                "sku": "SKU123",
                "weight": 1,
                "width": 10.0,
                "height": 10.0,
                "depth": 10.0,
                "warranty_information": "1 year",
                "shipping_information": "Free shipping",
                "availability_status": "In Stock",
                "return_policy": "30 days",
                "minimum_order_quantity": 1,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "barcode": "123456789",
                "qr_code": "https://example.com/qr.png",
                "thumbnail": "https://example.com/thumb.png",
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_products_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/products_update/1",
            {
                "title": "Updated Product",
                "description": "A great product",
                "category": "electronics",
                "price": 99.99,
                "discount_percentage": 10.0,
                "rating": 4.5,
                "stock": 100,
                "tags": "sale,new",
                "brand": "Brand",
                "sku": "SKU123",
                "weight": 1,
                "width": 10.0,
                "height": 10.0,
                "depth": 10.0,
                "warranty_information": "1 year",
                "shipping_information": "Free shipping",
                "availability_status": "In Stock",
                "return_policy": "30 days",
                "minimum_order_quantity": 1,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "barcode": "123456789",
                "qr_code": "https://example.com/qr.png",
                "thumbnail": "https://example.com/thumb.png",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_products_partial_update(self):
        response = self.client.patch(
            "/dummy_api/products_partial_update/1",
            {"price": 79.99},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_products_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/products_partial_update/1",
            {"price": 79.99},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_products_filter(self):
        response = self.client.get("/dummy_api/products_filter", {"category": "beauty"})
        self.assertEqual(response.status_code, 200)

    def test_products_delete(self):
        response = self.client.delete(
            "/dummy_api/products_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_products_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/products_delete/1",
        )
        self.assertEqual(response.status_code, 403)

    def test_reviews_list(self):
        response = self.client.get("/dummy_api/reviews_list")
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
                            "rating": {"type": "number"},
                            "comment": {"type": "string"},
                            "date": {"type": "string"},
                            "product": {"type": "number"},
                            "user": {"type": "number"},
                        },
                        "required": [
                            "id",
                            "rating",
                            "comment",
                            "date",
                            "product",
                            "user",
                        ],
                    },
                },
            )
        )

    def test_reviews_detail(self):
        response = self.client.get("/dummy_api/reviews_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "rating": {"type": "number"},
                        "comment": {"type": "string"},
                        "date": {"type": "string"},
                        "product": {"type": "number"},
                        "user": {"type": "number"},
                    },
                    "required": ["id", "rating", "comment", "date", "product", "user"],
                },
            )
        )

    def test_reviews_create(self):
        response = self.client.post(
            "/dummy_api/reviews_create",
            {
                "rating": 5,
                "comment": "Great product!",
                "date": "2024-01-01T00:00:00Z",
                "product": 1,
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_reviews_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/reviews_create",
            {
                "rating": 5,
                "comment": "Great product!",
                "date": "2024-01-01T00:00:00Z",
                "product": 1,
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_reviews_update(self):
        response = self.client.put(
            "/dummy_api/reviews_update/1",
            {
                "rating": 4,
                "comment": "Good product!",
                "date": "2024-01-01T00:00:00Z",
                "product": 1,
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_reviews_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/reviews_update/1",
            {
                "rating": 4,
                "comment": "Good product!",
                "date": "2024-01-01T00:00:00Z",
                "product": 1,
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_reviews_partial_update(self):
        response = self.client.patch(
            "/dummy_api/reviews_partial_update/1",
            {"rating": 5},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_reviews_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/reviews_partial_update/1",
            {"rating": 5},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_reviews_filter(self):
        response = self.client.get("/dummy_api/reviews_filter", {"rating": 5})
        self.assertEqual(response.status_code, 200)

    def test_reviews_delete(self):
        response = self.client.delete(
            "/dummy_api/reviews_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_reviews_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/reviews_delete/1",
        )
        self.assertEqual(response.status_code, 403)

    def test_posts_list(self):
        response = self.client.get("/dummy_api/posts_list")
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
                            "tags": {"type": "string"},
                            "likes": {"type": "number"},
                            "dislikes": {"type": "number"},
                            "views": {"type": "number"},
                            "user": {"type": "number"},
                        },
                        "required": [
                            "id",
                            "title",
                            "body",
                            "tags",
                            "likes",
                            "dislikes",
                            "views",
                            "user",
                        ],
                    },
                },
            )
        )

    def test_posts_detail(self):
        response = self.client.get("/dummy_api/posts_detail/1")
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
                        "tags": {"type": "string"},
                        "likes": {"type": "number"},
                        "dislikes": {"type": "number"},
                        "views": {"type": "number"},
                        "user": {"type": "number"},
                    },
                    "required": [
                        "id",
                        "title",
                        "body",
                        "tags",
                        "likes",
                        "dislikes",
                        "views",
                        "user",
                    ],
                },
            )
        )

    def test_posts_create(self):
        response = self.client.post(
            "/dummy_api/posts_create",
            {
                "title": "New Post",
                "body": "Post content",
                "tags": "news,update",
                "likes": 10,
                "dislikes": 1,
                "views": 100,
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_posts_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/posts_create",
            {
                "title": "New Post",
                "body": "Post content",
                "tags": "news,update",
                "likes": 10,
                "dislikes": 1,
                "views": 100,
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_posts_update(self):
        response = self.client.put(
            "/dummy_api/posts_update/1",
            {
                "title": "Updated Post",
                "body": "Post content",
                "tags": "news,update",
                "likes": 10,
                "dislikes": 1,
                "views": 100,
                "user": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_posts_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/posts_update/1",
            {
                "title": "Updated Post",
                "body": "Post content",
                "tags": "news,update",
                "likes": 10,
                "dislikes": 1,
                "views": 100,
                "user": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_posts_partial_update(self):
        response = self.client.patch(
            "/dummy_api/posts_partial_update/1",
            {"title": "New Title"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_posts_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/posts_partial_update/1",
            {"title": "New Title"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_posts_filter(self):
        response = self.client.get("/dummy_api/posts_filter", {"user": 1})
        self.assertEqual(response.status_code, 200)

    def test_posts_delete(self):
        response = self.client.delete(
            "/dummy_api/posts_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_posts_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/posts_delete/1",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_list(self):
        response = self.client.get("/dummy_api/comments_list")
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
                            "body": {"type": "string"},
                            "likes": {"type": "number"},
                            "post": {"type": "number"},
                        },
                        "required": ["id", "body", "likes", "post"],
                    },
                },
            )
        )

    def test_comments_detail(self):
        response = self.client.get("/dummy_api/comments_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "body": {"type": "string"},
                        "likes": {"type": "number"},
                        "post": {"type": "number"},
                    },
                    "required": ["id", "body", "likes", "post"],
                },
            )
        )

    def test_comments_create(self):
        response = self.client.post(
            "/dummy_api/comments_create",
            {
                "body": "New comment",
                "likes": 5,
                "post": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_comments_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/comments_create",
            {
                "body": "New comment",
                "likes": 5,
                "post": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_update(self):
        response = self.client.put(
            "/dummy_api/comments_update/1",
            {
                "body": "Updated comment",
                "likes": 5,
                "post": 1,
            },
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_comments_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/comments_update/1",
            {
                "body": "Updated comment",
                "likes": 5,
                "post": 1,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_partial_update(self):
        response = self.client.patch(
            "/dummy_api/comments_partial_update/1",
            {"body": "New body"},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_comments_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/comments_partial_update/1",
            {"body": "New body"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_comments_filter(self):
        response = self.client.get("/dummy_api/comments_filter", {"post": 1})
        self.assertEqual(response.status_code, 200)

    def test_comments_delete(self):
        response = self.client.delete(
            "/dummy_api/comments_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_comments_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/comments_delete/1",
        )
        self.assertEqual(response.status_code, 403)

    def test_carts_list(self):
        response = self.client.get("/dummy_api/carts_list")
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
                            "user": {"type": "number"},
                            "products": {"type": "array", "items": {"type": "number"}},
                        },
                        "required": ["id", "user", "products"],
                    },
                },
            )
        )

    def test_carts_detail(self):
        response = self.client.get("/dummy_api/carts_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(
            jsonschema.validate(
                response.json(),
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "user": {"type": "number"},
                        "products": {"type": "array", "items": {"type": "number"}},
                    },
                    "required": ["id", "user", "products"],
                },
            )
        )

    def test_carts_create(self):
        response = self.client.post(
            "/dummy_api/carts_create",
            {"user": 1, "products": [1, 2, 3]},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 201)

    def test_carts_create_forbidden(self):
        response = self.client.post(
            "/dummy_api/carts_create",
            {"user": 1, "products": [1, 2, 3]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_carts_update(self):
        response = self.client.put(
            "/dummy_api/carts_update/1",
            {"user": 1, "products": [1, 2]},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_carts_update_forbidden(self):
        response = self.client.put(
            "/dummy_api/carts_update/1",
            {"user": 1, "products": [1, 2]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_carts_partial_update(self):
        response = self.client.patch(
            "/dummy_api/carts_partial_update/1",
            {"products": [1]},
            content_type="application/json",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_carts_partial_update_forbidden(self):
        response = self.client.patch(
            "/dummy_api/carts_partial_update/1",
            {"products": [1]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 403)

    def test_carts_filter(self):
        response = self.client.get("/dummy_api/carts_filter", {"user": 1})
        self.assertEqual(response.status_code, 200)

    def test_carts_delete(self):
        response = self.client.delete(
            "/dummy_api/carts_delete/1",
            headers={"AUTH-TOKEN": settings.AUTH_TOKEN},
        )
        self.assertEqual(response.status_code, 200)

    def test_carts_delete_forbidden(self):
        response = self.client.delete(
            "/dummy_api/carts_delete/1",
        )
        self.assertEqual(response.status_code, 403)
