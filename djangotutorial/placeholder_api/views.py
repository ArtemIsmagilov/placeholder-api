from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import Comment, User, Todo, Album, Photo, Post


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


@api_view(["GET"])
def users_list(request: Request) -> Response:
    class UserOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        username = serializers.CharField()
        email = serializers.EmailField()
        address = serializers.CharField()
        phone = serializers.CharField()
        website = serializers.CharField()
        company = serializers.CharField()

    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(User.objects.order_by("id").all(), request)
    us = UserOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@api_view(["GET"])
def users_detail(request: Request, pk: int) -> Response:
    class UserOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        username = serializers.CharField()
        email = serializers.EmailField()
        address = serializers.CharField()
        phone = serializers.CharField()
        website = serializers.CharField()
        company = serializers.CharField()

    u = UserOutputSerializer(get_object_or_404(User, pk=pk))
    return Response(u.data)


@api_view(["GET"])
def users_search(request: Request) -> Response:
    class UserOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        username = serializers.CharField()
        email = serializers.EmailField()
        address = serializers.CharField()
        phone = serializers.CharField()
        website = serializers.CharField()
        company = serializers.CharField()

    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = User.objects.order_by("id")
    else:
        queryset = User.objects.filter(
            Q(id__icontains=q)
            | Q(name__icontains=q)
            | Q(username__icontains=q)
            | Q(email__icontains=q)
            | Q(address__icontains=q)
            | Q(phone__icontains=q)
            | Q(website__icontains=q)
            | Q(company__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = UserOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@api_view(["POST"])
def users_create(request: Request) -> Response:
    class UserInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        username = serializers.CharField()
        email = serializers.EmailField()
        address = serializers.CharField()
        phone = serializers.CharField()
        website = serializers.CharField()
        company = serializers.CharField()

    u = UserInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.create(**u.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def users_update(request: Request, pk: int) -> Response:
    class UserInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        username = serializers.CharField()
        email = serializers.EmailField()
        address = serializers.CharField()
        phone = serializers.CharField()
        website = serializers.CharField()
        company = serializers.CharField()

    u = UserInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
def users_partial_update(request: Request, pk: int) -> Response:
    class UserInputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        username = serializers.CharField(required=False)
        email = serializers.EmailField(required=False)
        address = serializers.CharField(required=False)
        phone = serializers.CharField(required=False)
        website = serializers.CharField(required=False)
        company = serializers.CharField(required=False)

    u = UserInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def todos_list(request: Request) -> Response:
    class TodoOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        completed = serializers.BooleanField()
        user = serializers.IntegerField(source="user_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Todo.objects.order_by("id").all(), request)
    ts = TodoOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@api_view(["GET"])
def todos_detail(request: Request, pk: int) -> Response:
    class TodoOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        completed = serializers.BooleanField()
        user = serializers.IntegerField(source="user_id")

    t = TodoOutputSerializer(get_object_or_404(Todo, pk=pk))
    return Response(t.data)


@api_view(["GET"])
def todos_search(request: Request) -> Response:
    class TodoOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        completed = serializers.BooleanField()
        user = serializers.IntegerField(source="user_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Todo.objects.order_by("id")
    else:
        queryset = Todo.objects.filter(
            Q(id__icontains=q)
            | Q(title__icontains=q)
            | Q(completed__icontains=q)
            | Q(user__id__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ts = TodoOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@api_view(["POST"])
def todos_create(request: Request) -> Response:
    class TodoInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        completed = serializers.BooleanField()
        user = serializers.IntegerField()

    t = TodoInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    body["user_id"] = body.pop("user")
    Todo.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def todos_update(request: Request, pk: int) -> Response:
    class TodoInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        completed = serializers.BooleanField()
        user = serializers.IntegerField()

    t = TodoInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    body["user_id"] = body.pop("user")
    Todo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
def todos_partial_update(request: Request, pk: int) -> Response:
    class TodoInputSerializer(serializers.Serializer):
        title = serializers.CharField(required=False)
        completed = serializers.BooleanField(required=False)
        user = serializers.IntegerField(required=False)

    t = TodoInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Todo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def albums_list(request: Request) -> Response:
    class AlbumOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        user = serializers.IntegerField(source="user_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Album.objects.order_by("id").all(), request)
    as_ = AlbumOutputSerializer(page, many=True)
    return paginator.get_paginated_response(as_.data)


@api_view(["GET"])
def albums_detail(request: Request, pk: int) -> Response:
    class AlbumOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        user = serializers.IntegerField(source="user_id")

    a = AlbumOutputSerializer(get_object_or_404(Album, pk=pk))
    return Response(a.data)


@api_view(["GET"])
def albums_search(request: Request) -> Response:
    class AlbumOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        user = serializers.IntegerField(source="user_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Album.objects.order_by("id")
    else:
        queryset = Album.objects.filter(
            Q(id__icontains=q) | Q(title__icontains=q) | Q(user__id__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    as_ = AlbumOutputSerializer(page, many=True)
    return paginator.get_paginated_response(as_.data)


@api_view(["POST"])
def albums_create(request: Request) -> Response:
    class AlbumInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        user = serializers.IntegerField()

    a = AlbumInputSerializer(data=request.data)
    a.is_valid(raise_exception=True)
    body = a.validated_data
    body["user_id"] = body.pop("user")
    Album.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def albums_update(request: Request, pk: int) -> Response:
    class AlbumInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        user = serializers.IntegerField()

    a = AlbumInputSerializer(data=request.data)
    a.is_valid(raise_exception=True)
    body = a.validated_data
    body["user_id"] = body.pop("user")
    Album.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
def albums_partial_update(request: Request, pk: int) -> Response:
    class AlbumInputSerializer(serializers.Serializer):
        title = serializers.CharField(required=False)
        user = serializers.IntegerField(required=False)

    a = AlbumInputSerializer(data=request.data)
    a.is_valid(raise_exception=True)
    body = a.validated_data
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Album.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def photos_list(request: Request) -> Response:
    class PhotoOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        url = serializers.URLField()
        thumbnail_url = serializers.URLField()
        album = serializers.IntegerField(source="album_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Photo.objects.order_by("id").all(), request)
    ps = PhotoOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@api_view(["GET"])
def photos_detail(request: Request, pk: int) -> Response:
    class PhotoOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        url = serializers.URLField()
        thumbnail_url = serializers.URLField()
        album = serializers.IntegerField(source="album_id")

    p = PhotoOutputSerializer(get_object_or_404(Photo, pk=pk))
    return Response(p.data)


@api_view(["GET"])
def photos_search(request: Request) -> Response:
    class PhotoOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        url = serializers.URLField()
        thumbnail_url = serializers.URLField()
        album = serializers.IntegerField(source="album_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Photo.objects.order_by("id")
    else:
        queryset = Photo.objects.filter(
            Q(id__icontains=q)
            | Q(title__icontains=q)
            | Q(url__icontains=q)
            | Q(thumbnail_url__icontains=q)
            | Q(album__id__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = PhotoOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@api_view(["POST"])
def photos_create(request: Request) -> Response:
    class PhotoInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        url = serializers.URLField()
        thumbnail_url = serializers.URLField()
        album = serializers.IntegerField()

    p = PhotoInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["album_id"] = body.pop("album")
    Photo.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def photos_update(request: Request, pk: int) -> Response:
    class PhotoInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        url = serializers.URLField()
        thumbnail_url = serializers.URLField()
        album = serializers.IntegerField()

    p = PhotoInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["album_id"] = body.pop("album")
    Photo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
def photos_partial_update(request: Request, pk: int) -> Response:
    class PhotoInputSerializer(serializers.Serializer):
        title = serializers.CharField(required=False)
        url = serializers.URLField(required=False)
        thumbnail_url = serializers.URLField(required=False)
        album = serializers.IntegerField(required=False)

    p = PhotoInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    if body.get("album") is not None:
        body["album_id"] = body.pop("album")
    Photo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def posts_list(request: Request) -> Response:
    class PostOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        body = serializers.CharField()
        user = serializers.IntegerField(source="user_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Post.objects.order_by("id").all(), request)
    ps = PostOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@api_view(["GET"])
def posts_detail(request: Request, pk: int) -> Response:
    class PostOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        body = serializers.CharField()
        user = serializers.IntegerField(source="user_id")

    p = PostOutputSerializer(get_object_or_404(Post, pk=pk))
    return Response(p.data)


@api_view(["GET"])
def posts_search(request: Request) -> Response:
    class PostOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        body = serializers.CharField()
        user = serializers.IntegerField(source="user_id")

    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Post.objects.order_by("id")
    else:
        queryset = Post.objects.filter(
            Q(id__icontains=q)
            | Q(title__icontains=q)
            | Q(body__icontains=q)
            | Q(user__id__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = PostOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@api_view(["POST"])
def posts_create(request: Request) -> Response:
    class PostInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        body = serializers.CharField()
        user = serializers.IntegerField()

    p = PostInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["user_id"] = body.pop("user")
    Post.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def posts_update(request: Request, pk: int) -> Response:
    class PostInputSerializer(serializers.Serializer):
        title = serializers.CharField()
        body = serializers.CharField()
        user = serializers.IntegerField()

    p = PostInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["user_id"] = body.pop("user")
    Post.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
def posts_partial_update(request: Request, pk: int) -> Response:
    class PostInputSerializer(serializers.Serializer):
        title = serializers.CharField(required=False)
        body = serializers.CharField(required=False)
        user = serializers.IntegerField(required=False)

    p = PostInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Post.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)
