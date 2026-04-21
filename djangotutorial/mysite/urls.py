"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import sys

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from placeholder_api import views
from dummy_api import views as dummy_views


urlpatterns = [
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("placeholder_api/comments_list", views.comments_list, name="comments_list"),
    path(
        "placeholder_api/comments_detail/<int:pk>",
        views.comments_detail,
        name="comments_detail",
    ),
    path(
        "placeholder_api/comments_search", views.comments_search, name="comments_search"
    ),
    path(
        "placeholder_api/comments_create", views.comments_create, name="comments_create"
    ),
    path(
        "placeholder_api/comments_update/<int:pk>",
        views.comments_update,
        name="comments_update",
    ),
    path(
        "placeholder_api/comments_partial_update/<int:pk>",
        views.comments_partial_update,
        name="comments_partial_update",
    ),
    path(
        "placeholder_api/comments_filter",
        views.comments_filter,
        name="comments_filter",
    ),
    path(
        "placeholder_api/comments_delete/<int:pk>",
        views.comments_delete,
        name="comments_delete",
    ),
    path("placeholder_api/users_list", views.users_list, name="users_list"),
    path(
        "placeholder_api/users_detail/<int:pk>", views.users_detail, name="users_detail"
    ),
    path("placeholder_api/users_search", views.users_search, name="users_search"),
    path("placeholder_api/users_create", views.users_create, name="users_create"),
    path(
        "placeholder_api/users_update/<int:pk>", views.users_update, name="users_update"
    ),
    path(
        "placeholder_api/users_partial_update/<int:pk>",
        views.users_partial_update,
        name="users_partial_update",
    ),
    path("placeholder_api/users_filter", views.users_filter, name="users_filter"),
    path(
        "placeholder_api/users_delete/<int:pk>",
        views.users_delete,
        name="users_delete",
    ),
    path("placeholder_api/todos_list", views.todos_list, name="todos_list"),
    path(
        "placeholder_api/todos_detail/<int:pk>", views.todos_detail, name="todos_detail"
    ),
    path("placeholder_api/todos_search", views.todos_search, name="todos_search"),
    path("placeholder_api/todos_create", views.todos_create, name="todos_create"),
    path(
        "placeholder_api/todos_update/<int:pk>", views.todos_update, name="todos_update"
    ),
    path(
        "placeholder_api/todos_partial_update/<int:pk>",
        views.todos_partial_update,
        name="todos_partial_update",
    ),
    path("placeholder_api/todos_filter", views.todos_filter, name="todos_filter"),
    path(
        "placeholder_api/todos_delete/<int:pk>",
        views.todos_delete,
        name="todos_delete",
    ),
    path("placeholder_api/albums_list", views.albums_list, name="albums_list"),
    path(
        "placeholder_api/albums_detail/<int:pk>",
        views.albums_detail,
        name="albums_detail",
    ),
    path("placeholder_api/albums_search", views.albums_search, name="albums_search"),
    path("placeholder_api/albums_create", views.albums_create, name="albums_create"),
    path(
        "placeholder_api/albums_update/<int:pk>",
        views.albums_update,
        name="albums_update",
    ),
    path(
        "placeholder_api/albums_partial_update/<int:pk>",
        views.albums_partial_update,
        name="albums_partial_update",
    ),
    path("placeholder_api/albums_filter", views.albums_filter, name="albums_filter"),
    path(
        "placeholder_api/albums_delete/<int:pk>",
        views.albums_delete,
        name="albums_delete",
    ),
    path("placeholder_api/photos_list", views.photos_list, name="photos_list"),
    path(
        "placeholder_api/photos_detail/<int:pk>",
        views.photos_detail,
        name="photos_detail",
    ),
    path("placeholder_api/photos_search", views.photos_search, name="photos_search"),
    path("placeholder_api/photos_create", views.photos_create, name="photos_create"),
    path(
        "placeholder_api/photos_update/<int:pk>",
        views.photos_update,
        name="photos_update",
    ),
    path(
        "placeholder_api/photos_partial_update/<int:pk>",
        views.photos_partial_update,
        name="photos_partial_update",
    ),
    path("placeholder_api/photos_filter", views.photos_filter, name="photos_filter"),
    path(
        "placeholder_api/photos_delete/<int:pk>",
        views.photos_delete,
        name="photos_delete",
    ),
    path("placeholder_api/posts_list", views.posts_list, name="posts_list"),
    path(
        "placeholder_api/posts_detail/<int:pk>", views.posts_detail, name="posts_detail"
    ),
    path("placeholder_api/posts_search", views.posts_search, name="posts_search"),
    path("placeholder_api/posts_create", views.posts_create, name="posts_create"),
    path(
        "placeholder_api/posts_update/<int:pk>", views.posts_update, name="posts_update"
    ),
    path(
        "placeholder_api/posts_partial_update/<int:pk>",
        views.posts_partial_update,
        name="posts_partial_update",
    ),
    path("placeholder_api/posts_filter", views.posts_filter, name="posts_filter"),
    path(
        "placeholder_api/posts_delete/<int:pk>",
        views.posts_delete,
        name="posts_delete",
    ),
    path("placeholder_api/profile/<int:pk>", views.profile, name="profile"),
    path("placeholder_api/healthcheck", views.healthcheck, name="healthcheck"),
    path("dummy_api/users_list", dummy_views.users_list, name="users_list"),
    path(
        "dummy_api/users_detail/<int:pk>", dummy_views.users_detail, name="users_detail"
    ),
    path("dummy_api/users_search", dummy_views.users_search, name="users_search"),
    path("dummy_api/users_create", dummy_views.users_create, name="users_create"),
    path(
        "dummy_api/users_update/<int:pk>", dummy_views.users_update, name="users_update"
    ),
    path(
        "dummy_api/users_partial_update/<int:pk>",
        dummy_views.users_partial_update,
        name="users_partial_update",
    ),
    path("dummy_api/users_filter", dummy_views.users_filter, name="users_filter"),
    path(
        "dummy_api/users_delete/<int:pk>", dummy_views.users_delete, name="users_delete"
    ),
    path("dummy_api/todos_list", dummy_views.todos_list, name="todos_list"),
    path(
        "dummy_api/todos_detail/<int:pk>", dummy_views.todos_detail, name="todos_detail"
    ),
    path("dummy_api/todos_search", dummy_views.todos_search, name="todos_search"),
    path("dummy_api/todos_create", dummy_views.todos_create, name="todos_create"),
    path(
        "dummy_api/todos_update/<int:pk>", dummy_views.todos_update, name="todos_update"
    ),
    path(
        "dummy_api/todos_partial_update/<int:pk>",
        dummy_views.todos_partial_update,
        name="todos_partial_update",
    ),
    path("dummy_api/todos_filter", dummy_views.todos_filter, name="todos_filter"),
    path(
        "dummy_api/todos_delete/<int:pk>", dummy_views.todos_delete, name="todos_delete"
    ),
    path("dummy_api/recipes_list", dummy_views.recipes_list, name="recipes_list"),
    path(
        "dummy_api/recipes_detail/<int:pk>",
        dummy_views.recipes_detail,
        name="recipes_detail",
    ),
    path("dummy_api/recipes_search", dummy_views.recipes_search, name="recipes_search"),
    path("dummy_api/recipes_create", dummy_views.recipes_create, name="recipes_create"),
    path(
        "dummy_api/recipes_update/<int:pk>",
        dummy_views.recipes_update,
        name="recipes_update",
    ),
    path(
        "dummy_api/recipes_partial_update/<int:pk>",
        dummy_views.recipes_partial_update,
        name="recipes_partial_update",
    ),
    path("dummy_api/recipes_filter", dummy_views.recipes_filter, name="recipes_filter"),
    path(
        "dummy_api/recipes_delete/<int:pk>",
        dummy_views.recipes_delete,
        name="recipes_delete",
    ),
    path("dummy_api/quotes_list", dummy_views.quotes_list, name="quotes_list"),
    path(
        "dummy_api/quotes_detail/<int:pk>",
        dummy_views.quotes_detail,
        name="quotes_detail",
    ),
    path("dummy_api/quotes_search", dummy_views.quotes_search, name="quotes_search"),
    path("dummy_api/quotes_create", dummy_views.quotes_create, name="quotes_create"),
    path(
        "dummy_api/quotes_update/<int:pk>",
        dummy_views.quotes_update,
        name="quotes_update",
    ),
    path(
        "dummy_api/quotes_partial_update/<int:pk>",
        dummy_views.quotes_partial_update,
        name="quotes_partial_update",
    ),
    path("dummy_api/quotes_filter", dummy_views.quotes_filter, name="quotes_filter"),
    path(
        "dummy_api/quotes_delete/<int:pk>",
        dummy_views.quotes_delete,
        name="quotes_delete",
    ),
    path("dummy_api/products_list", dummy_views.products_list, name="products_list"),
    path(
        "dummy_api/products_detail/<int:pk>",
        dummy_views.products_detail,
        name="products_detail",
    ),
    path(
        "dummy_api/products_search", dummy_views.products_search, name="products_search"
    ),
    path(
        "dummy_api/products_create", dummy_views.products_create, name="products_create"
    ),
    path(
        "dummy_api/products_update/<int:pk>",
        dummy_views.products_update,
        name="products_update",
    ),
    path(
        "dummy_api/products_partial_update/<int:pk>",
        dummy_views.products_partial_update,
        name="products_partial_update",
    ),
    path(
        "dummy_api/products_filter", dummy_views.products_filter, name="products_filter"
    ),
    path(
        "dummy_api/products_delete/<int:pk>",
        dummy_views.products_delete,
        name="products_delete",
    ),
    path("dummy_api/reviews_list", dummy_views.reviews_list, name="reviews_list"),
    path(
        "dummy_api/reviews_detail/<int:pk>",
        dummy_views.reviews_detail,
        name="reviews_detail",
    ),
    path("dummy_api/reviews_search", dummy_views.reviews_search, name="reviews_search"),
    path("dummy_api/reviews_create", dummy_views.reviews_create, name="reviews_create"),
    path(
        "dummy_api/reviews_update/<int:pk>",
        dummy_views.reviews_update,
        name="reviews_update",
    ),
    path(
        "dummy_api/reviews_partial_update/<int:pk>",
        dummy_views.reviews_partial_update,
        name="reviews_partial_update",
    ),
    path("dummy_api/reviews_filter", dummy_views.reviews_filter, name="reviews_filter"),
    path(
        "dummy_api/reviews_delete/<int:pk>",
        dummy_views.reviews_delete,
        name="reviews_delete",
    ),
    path("dummy_api/posts_list", dummy_views.posts_list, name="posts_list"),
    path(
        "dummy_api/posts_detail/<int:pk>", dummy_views.posts_detail, name="posts_detail"
    ),
    path("dummy_api/posts_search", dummy_views.posts_search, name="posts_search"),
    path("dummy_api/posts_create", dummy_views.posts_create, name="posts_create"),
    path(
        "dummy_api/posts_update/<int:pk>", dummy_views.posts_update, name="posts_update"
    ),
    path(
        "dummy_api/posts_partial_update/<int:pk>",
        dummy_views.posts_partial_update,
        name="posts_partial_update",
    ),
    path("dummy_api/posts_filter", dummy_views.posts_filter, name="posts_filter"),
    path(
        "dummy_api/posts_delete/<int:pk>", dummy_views.posts_delete, name="posts_delete"
    ),
    path("dummy_api/comments_list", dummy_views.comments_list, name="comments_list"),
    path(
        "dummy_api/comments_detail/<int:pk>",
        dummy_views.comments_detail,
        name="comments_detail",
    ),
    path(
        "dummy_api/comments_search", dummy_views.comments_search, name="comments_search"
    ),
    path(
        "dummy_api/comments_create", dummy_views.comments_create, name="comments_create"
    ),
    path(
        "dummy_api/comments_update/<int:pk>",
        dummy_views.comments_update,
        name="comments_update",
    ),
    path(
        "dummy_api/comments_partial_update/<int:pk>",
        dummy_views.comments_partial_update,
        name="comments_partial_update",
    ),
    path(
        "dummy_api/comments_filter", dummy_views.comments_filter, name="comments_filter"
    ),
    path(
        "dummy_api/comments_delete/<int:pk>",
        dummy_views.comments_delete,
        name="comments_delete",
    ),
    path("dummy_api/carts_list", dummy_views.carts_list, name="carts_list"),
    path(
        "dummy_api/carts_detail/<int:pk>", dummy_views.carts_detail, name="carts_detail"
    ),
    path("dummy_api/carts_search", dummy_views.carts_search, name="carts_search"),
    path("dummy_api/carts_create", dummy_views.carts_create, name="carts_create"),
    path(
        "dummy_api/carts_update/<int:pk>", dummy_views.carts_update, name="carts_update"
    ),
    path(
        "dummy_api/carts_partial_update/<int:pk>",
        dummy_views.carts_partial_update,
        name="carts_partial_update",
    ),
    path("dummy_api/carts_filter", dummy_views.carts_filter, name="carts_filter"),
    path(
        "dummy_api/carts_delete/<int:pk>", dummy_views.carts_delete, name="carts_delete"
    ),
]

if "test" not in sys.argv and settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns.extend(debug_toolbar_urls())
