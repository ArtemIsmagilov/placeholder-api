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

from placeholder_api import views


urlpatterns = [
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
]
