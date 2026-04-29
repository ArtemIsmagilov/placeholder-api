import csv
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Count
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_spectacular.utils import (
    extend_schema,
    inline_serializer,
    OpenApiParameter,
    OpenApiTypes,
)

from mysite.base_permissions import TokenPermission
from .models import Comment, User, Todo, Album, Photo, Post
from .serializers.comments_serializers import (
    CommentSearchOutputSerializer,
    CommentListOutputSerializer,
    CommentDetailOutputSerializer,
    CommentCreateInputSerializer,
    CommentUpdateInputSerializer,
    CommentPartialUpdateInputSerializer,
    CommentFilterOutputSerializer,
    CommentFilterInputSerializer,
    CommentStatsOutputSerializer,
)
from .serializers.users_serializers import (
    UserSearchOutputSerializer,
    UserListOutputSerializer,
    UserDetailOutputSerializer,
    UserCreateInputSerializer,
    UserUpdateInputSerializer,
    UserPartialUpdateInputSerializer,
    UserFilterOutputSerializer,
    UserFilterInputSerializer,
    UserStatsOutputSerializer,
)
from .serializers.todos_serializers import (
    TodoSearchOutputSerializer,
    TodoListOutputSerializer,
    TodoDetailOutputSerializer,
    TodoCreateInputSerializer,
    TodoUpdateInputSerializer,
    TodoPartialUpdateInputSerializer,
    TodoFilterOutputSerializer,
    TodoFilterInputSerializer,
    TodoStatsOutputSerializer,
)
from .serializers.albums_serializers import (
    AlbumSearchOutputSerializer,
    AlbumListOutputSerializer,
    AlbumDetailOutputSerializer,
    AlbumCreateInputSerializer,
    AlbumUpdateInputSerializer,
    AlbumPartialUpdateInputSerializer,
    AlbumFilterOutputSerializer,
    AlbumFilterInputSerializer,
    AlbumStatsOutputSerializer,
)
from .serializers.photos_serializers import (
    PhotoSearchOutputSerializer,
    PhotoListOutputSerializer,
    PhotoDetailOutputSerializer,
    PhotoCreateInputSerializer,
    PhotoUpdateInputSerializer,
    PhotoPartialUpdateInputSerializer,
    PhotoFilterOutputSerializer,
    PhotoFilterInputSerializer,
    PhotoStatsOutputSerializer,
)
from .serializers.posts_serializers import (
    PostSearchOutputSerializer,
    PostListOutputSerializer,
    PostDetailOutputSerializer,
    PostCreateInputSerializer,
    PostUpdateInputSerializer,
    PostPartialUpdateInputSerializer,
    PostFilterOutputSerializer,
    PostFilterInputSerializer,
    PostStatsOutputSerializer,
)
from .serializers.profile_serializers import ProfileOutputSerializer


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineCommentListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": CommentListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def comments_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Comment.objects.order_by("id"), request)
    cs = CommentListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: CommentDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def comments_detail(request: Request, pk: int) -> Response:
    c = CommentDetailOutputSerializer(get_object_or_404(Comment, pk=pk))
    return Response(c.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineCommentSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": CommentSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def comments_search(request: Request) -> Response:
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
    cs = CommentSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    request=CommentCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def comments_create(request: Request) -> Response:
    c = CommentCreateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["post_id"] = body.pop("post")
    Comment.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=CommentUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: None,
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def comments_update(request: Request, pk: int) -> Response:
    c = CommentUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["post_id"] = body.pop("post")
    Comment.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=CommentPartialUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: None,
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def comments_partial_update(request: Request, pk: int) -> Response:
    c = CommentPartialUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    if body.get("post") is not None:
        body["post_id"] = body.pop("post")
    Comment.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineCommentFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": CommentFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="name", description="Filter by name", type=str),
        OpenApiParameter("email", description="Filter by email", type=str),
        OpenApiParameter("body", description="Filter by body", type=str),
        OpenApiParameter("post", description="Filter by post", type=int),
    ],
)
@api_view(["GET"])
def comments_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = CommentFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Comment.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)
    if (q := validated_data.get("email")) is not None:
        queryset = queryset.filter(email=q)
    if (q := validated_data.get("body")) is not None:
        queryset = queryset.filter(body=q)
    if (q := validated_data.get("post")) is not None:
        queryset = queryset.filter(post=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = CommentFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: None,
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def comments_delete(request: Request, pk: int) -> Response:
    Comment.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineUserListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": UserListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def users_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(User.objects.order_by("id").all(), request)
    us = UserListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    responses={
        200: UserDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def users_detail(request: Request, pk: int) -> Response:
    u = UserDetailOutputSerializer(get_object_or_404(User, pk=pk))
    return Response(u.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineUserSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": UserSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def users_search(request: Request) -> Response:
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
    us = UserSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    request=UserCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def users_create(request: Request) -> Response:
    u = UserCreateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.create(**u.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=UserUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def users_update(request: Request, pk: int) -> Response:
    u = UserUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=UserPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def users_partial_update(request: Request, pk: int) -> Response:
    u = UserPartialUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineUserFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": UserFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="name", description="Filter by name", type=str),
        OpenApiParameter(name="username", description="Filter by username", type=str),
        OpenApiParameter(name="email", description="Filter by email", type=str),
        OpenApiParameter(name="address", description="Filter by address", type=str),
        OpenApiParameter(name="phone", description="Filter by phone", type=str),
        OpenApiParameter(name="website", description="Filter by website", type=str),
        OpenApiParameter(name="company", description="Filter by company", type=str),
    ],
)
@api_view(["GET"])
def users_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = UserFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = User.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)
    if (q := validated_data.get("username")) is not None:
        queryset = queryset.filter(username=q)
    if (q := validated_data.get("email")) is not None:
        queryset = queryset.filter(email=q)
    if (q := validated_data.get("address")) is not None:
        queryset = queryset.filter(address=q)
    if (q := validated_data.get("phone")) is not None:
        queryset = queryset.filter(phone=q)
    if (q := validated_data.get("website")) is not None:
        queryset = queryset.filter(website=q)
    if (q := validated_data.get("company")) is not None:
        queryset = queryset.filter(company=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = UserFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def users_delete(request: Request, pk: int) -> Response:
    User.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineTodoListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TodoListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def todos_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Todo.objects.order_by("id").all(), request)
    ts = TodoListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@extend_schema(
    responses={
        200: TodoDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def todos_detail(request: Request, pk: int) -> Response:
    t = TodoDetailOutputSerializer(get_object_or_404(Todo, pk=pk))
    return Response(t.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineTodoSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TodoSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def todos_search(request: Request) -> Response:
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
    ts = TodoSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@extend_schema(
    request=TodoCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def todos_create(request: Request) -> Response:
    t = TodoCreateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    body["user_id"] = body.pop("user")
    Todo.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TodoUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def todos_update(request: Request, pk: int) -> Response:
    t = TodoUpdateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    body["user_id"] = body.pop("user")
    Todo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TodoPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def todos_partial_update(request: Request, pk: int) -> Response:
    t = TodoPartialUpdateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Todo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineTodoFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TodoFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(
            name="completed",
            description="Filter by completed",
            type=bool,
        ),
        OpenApiParameter(name="user", description="Filter by user", type=int),
    ],
)
@api_view(["GET"])
def todos_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TodoFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Todo.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("title")) is not None:
        queryset = queryset.filter(title=q)
    if (q := validated_data.get("completed")) is not None:
        queryset = queryset.filter(completed=q)
    if (q := validated_data.get("user")) is not None:
        queryset = queryset.filter(user=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ts = TodoFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def todos_delete(request: Request, pk: int) -> Response:
    Todo.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineAlbumListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": AlbumListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def albums_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Album.objects.order_by("id").all(), request)
    as_ = AlbumListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(as_.data)


@extend_schema(
    responses={
        200: AlbumDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def albums_detail(request: Request, pk: int) -> Response:
    a = AlbumDetailOutputSerializer(get_object_or_404(Album, pk=pk))
    return Response(a.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineAlbumSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": AlbumSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def albums_search(request: Request) -> Response:
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
    as_ = AlbumSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(as_.data)


@extend_schema(
    request=AlbumCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def albums_create(request: Request) -> Response:
    a = AlbumCreateInputSerializer(data=request.data)
    a.is_valid(raise_exception=True)
    body = a.validated_data
    body["user_id"] = body.pop("user")
    Album.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=AlbumUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def albums_update(request: Request, pk: int) -> Response:
    a = AlbumUpdateInputSerializer(data=request.data)
    a.is_valid(raise_exception=True)
    body = a.validated_data
    body["user_id"] = body.pop("user")
    Album.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=AlbumPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def albums_partial_update(request: Request, pk: int) -> Response:
    a = AlbumPartialUpdateInputSerializer(data=request.data)
    a.is_valid(raise_exception=True)
    body = a.validated_data
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Album.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlineAlbumFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": AlbumFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(name="user", description="Filter by user", type=int),
    ],
)
@api_view(["GET"])
def albums_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = AlbumFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Album.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("title")) is not None:
        queryset = queryset.filter(title=q)
    if (q := validated_data.get("user")) is not None:
        queryset = queryset.filter(user=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    as_ = AlbumFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(as_.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def albums_delete(request: Request, pk: int) -> Response:
    Album.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlinePhotoListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": PhotoListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def photos_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Photo.objects.order_by("id").all(), request)
    ps = PhotoListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={
        200: PhotoDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def photos_detail(request: Request, pk: int) -> Response:
    p = PhotoDetailOutputSerializer(get_object_or_404(Photo, pk=pk))
    return Response(p.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlinePhotoSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": PhotoSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def photos_search(request: Request) -> Response:
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
    ps = PhotoSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    request=PhotoCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def photos_create(request: Request) -> Response:
    p = PhotoCreateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["album_id"] = body.pop("album")
    Photo.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=PhotoUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def photos_update(request: Request, pk: int) -> Response:
    p = PhotoUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["album_id"] = body.pop("album")
    Photo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=PhotoPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def photos_partial_update(request: Request, pk: int) -> Response:
    p = PhotoPartialUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    if body.get("album") is not None:
        body["album_id"] = body.pop("album")
    Photo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlinePhotoFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": PhotoFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(name="url", description="Filter by url", type=str),
        OpenApiParameter(
            name="thumbnail_url",
            description="Filter by thumbnail_url",
            type=str,
        ),
        OpenApiParameter(name="album", description="Filter by album", type=int),
    ],
)
@api_view(["GET"])
def photos_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = PhotoFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Photo.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("title")) is not None:
        queryset = queryset.filter(title=q)
    if (q := validated_data.get("url")) is not None:
        queryset = queryset.filter(url=q)
    if (q := validated_data.get("thumbnail_url")) is not None:
        queryset = queryset.filter(thumbnail_url=q)
    if (q := validated_data.get("album")) is not None:
        queryset = queryset.filter(album=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = PhotoFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def photos_delete(request: Request, pk: int) -> Response:
    Photo.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlinePostListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": PostListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def posts_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Post.objects.order_by("id").all(), request)
    ps = PostListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={
        200: PostDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def posts_detail(request: Request, pk: int) -> Response:
    p = PostDetailOutputSerializer(get_object_or_404(Post, pk=pk))
    return Response(p.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlinePostSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": PostSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def posts_search(request: Request) -> Response:
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
    ps = PostSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    request=PostCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def posts_create(request: Request) -> Response:
    p = PostCreateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["user_id"] = body.pop("user")
    Post.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=PostUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def posts_update(request: Request, pk: int) -> Response:
    p = PostUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["user_id"] = body.pop("user")
    Post.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=PostPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def posts_partial_update(request: Request, pk: int) -> Response:
    p = PostPartialUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Post.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "InlinePostFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": PostFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(name="body", description="Filter by body", type=str),
        OpenApiParameter(name="user", description="Filter by user", type=int),
    ],
)
@api_view(["GET"])
def posts_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = PostFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Post.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("title")) is not None:
        queryset = queryset.filter(title=q)
    if (q := validated_data.get("body")) is not None:
        queryset = queryset.filter(body=q)
    if (q := validated_data.get("user")) is not None:
        queryset = queryset.filter(user=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = PostFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def posts_delete(request: Request, pk: int) -> Response:
    Post.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(responses={status.HTTP_200_OK: ProfileOutputSerializer()})
@api_view(["GET"])
def profile(request: Request, pk: int) -> Response:
    queryset = User.objects.prefetch_related(
        "todo_set", "album_set__photo_set", "post_set__comment_set"
    )
    user = get_object_or_404(queryset, id=pk)

    user_data = {
        "user_info": {
            "name": user.name,
            "username": user.username,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
            "website": user.website,
            "company": user.company,
        },
        "todos": [
            {"title": todo.title, "completed": todo.completed}
            for todo in user.todo_set.all()
        ],
        "albums": [
            {
                "title": album.title,
                "pictures": [
                    {
                        "title": photo.title,
                        "url": photo.url,
                        "thumbnail_url": photo.thumbnail_url,
                    }
                    for photo in album.photo_set.all()
                ],
            }
            for album in user.album_set.all()
        ],
        "posts": [
            {
                "title": post.title,
                "body": post.body,
                "comments": [
                    {
                        "name": comment.name,
                        "email": comment.email,
                        "body": comment.body,
                    }
                    for comment in post.comment_set.all()
                ],
            }
            for post in user.post_set.all()
        ],
    }
    serializer = ProfileOutputSerializer(user_data)
    return Response(serializer.data)


@extend_schema(responses={status.HTTP_200_OK: None})
@api_view(["GET"])
def healthcheck(request: Request) -> Response:
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={status.HTTP_200_OK: UserStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def users_stats(request: Request) -> Response:
    data = (
        User.objects.values("company")
        .annotate(count_users=Count("id"))
        .order_by("-count_users")
    )
    serializer = UserStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TodoStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def todos_stats(request: Request) -> Response:
    data = (
        Todo.objects.values("user_id")
        .annotate(
            count_todos=Count("id"),
            count_completed=Count("id", filter=Q(completed=True)),
            count_uncompleted=Count("id", filter=Q(completed=False)),
        )
        .order_by("-count_completed")
    )
    serializer = TodoStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: AlbumStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def albums_stats(request: Request) -> Response:
    data = (
        Album.objects.values("user_id")
        .annotate(count_albums=Count("id"))
        .order_by("-count_albums")
    )
    serializer = AlbumStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: PhotoStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def photos_stats(request: Request) -> Response:
    data = (
        Photo.objects.values("album_id")
        .annotate(count_photos=Count("id"))
        .order_by("-count_photos")
    )
    serializer = PhotoStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: PostStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def posts_stats(request: Request) -> Response:
    data = (
        Post.objects.values("user_id")
        .annotate(count_posts=Count("id"))
        .order_by("-count_posts")
    )
    serializer = PostStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: CommentStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def comments_stats(request: Request) -> Response:
    data = (
        Comment.objects.values("post_id")
        .annotate(count_comments=Count("id"))
        .order_by("-count_comments")
    )
    serializer = CommentStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(responses={(status.HTTP_200_OK, "*/*"): OpenApiTypes.BINARY})
@api_view(["GET"])
def profiles_export_csv(request: Request) -> HttpResponse:
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="users.csv"'},
    )

    writer = csv.writer(response)

    queryset = User.objects.prefetch_related(
        "todo_set", "album_set__photo_set", "post_set__comment_set"
    )

    for user in queryset:
        writer.writerow(["user_info"])
        writer.writerow(
            ["name", "username", "email", "address", "phone", "website", "company"]
        )
        writer.writerow(
            [
                user.name,
                user.username,
                user.email,
                user.address,
                user.phone,
                user.website,
                user.company,
            ]
        )
        writer.writerow([])
        writer.writerow(["todos"])
        writer.writerow(["title", "completed"])
        for todo in user.todo_set.all():
            writer.writerow([todo.title, todo.completed])
        writer.writerow([])
        writer.writerow(["albums"])
        writer.writerow(["title"])
        for album in user.album_set.all():
            writer.writerow([album.title])
            writer.writerow(["pictures"])
            writer.writerow(["title", "url", "thumbnail_url"])
            for photo in album.photo_set.all():
                writer.writerow([photo.title, photo.url, photo.thumbnail_url])
        writer.writerow([])
        writer.writerow(["posts"])
        writer.writerow(["title", "body"])
        for post in user.post_set.all():
            writer.writerow([post.title, post.body])
            writer.writerow(["comments"])
            writer.writerow(["name", "email", "body"])
            for comment in post.comment_set.all():
                writer.writerow([comment.name, comment.email, comment.body])
        writer.writerow([])

    return response
