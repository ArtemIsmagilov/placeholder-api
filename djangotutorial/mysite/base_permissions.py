from typing import Any
from django.conf import settings
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class TokenPermission(BasePermission):
    def has_permission(self, request: Request, view: Any) -> bool:
        if request.method in SAFE_METHODS:
            return True
        token = request.headers.get("AUTH-TOKEN")
        return token is not None and token == settings.AUTH_TOKEN
