from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import Comment


@api_view(["GET"])
def comments_list(request: Request) -> Response:
    class CommentOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        email = serializers.EmailField()
        body = serializers.CharField()
        post = serializers.IntegerField(source="post_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Comment.objects.order_by("id").all(), request)
    cs = CommentOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@api_view(["GET"])
def comments_detail(request: Request, pk: int) -> Response:
    class CommentOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        email = serializers.EmailField()
        body = serializers.CharField()
        post = serializers.IntegerField(source="post_id")

    c = CommentOutputSerializer(get_object_or_404(Comment, pk=pk))
    return Response(c.data)


@api_view(["GET"])
def comments_search(request: Request) -> Response:
    class CommentOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        email = serializers.EmailField()
        body = serializers.CharField()
        post = serializers.IntegerField(source="post_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Comment.objects.order_by("id")
    else:
        queryset = Comment.objects.filter(
            Q(id__icontains=q)
            | Q(name__icontains=q)
            | Q(email__icontains=q)
            | Q(body__icontains=q)
            | Q(post__id__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = CommentOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@api_view(["POST"])
def comments_create(request: Request) -> Response:
    class CommentInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        email = serializers.EmailField()
        body = serializers.CharField()
        post = serializers.IntegerField()

    c = CommentInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["post_id"] = body.pop("post")
    Comment.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def comments_update(request: Request, pk: int) -> Response:
    class CommentInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        email = serializers.EmailField()
        body = serializers.CharField()
        post = serializers.IntegerField()

    c = CommentInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["post_id"] = body.pop("post")
    Comment.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
def comments_partial_update(request: Request, pk: int) -> Response:
    class CommentInputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        email = serializers.EmailField(required=False)
        body = serializers.CharField(required=False)
        post = serializers.IntegerField(required=False)

    c = CommentInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    if body.get("post") is not None:
        body["post_id"] = body.pop("post")
    Comment.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)
