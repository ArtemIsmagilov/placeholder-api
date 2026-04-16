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

from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from placeholder_api import views


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
]
