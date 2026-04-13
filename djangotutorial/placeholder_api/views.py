from rest_framework.request import Request
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import Comment


# Create your views here.
@api_view(["GET"])
def comments_list(request: Request):
    class CommentSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        email = serializers.EmailField()
        body = serializers.CharField()
        post = serializers.IntegerField(source="post_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Comment.objects.order_by("id").all(), request)
    cs = CommentSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)
