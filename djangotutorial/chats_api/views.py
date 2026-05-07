from django.shortcuts import get_object_or_404
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
)

from mysite.base_permissions import TokenPermission
from .models import User, Chat, Message
from .serializers.users_serializers import (
    ChatsUserSearchOutputSerializer,
    ChatsUserListOutputSerializer,
    ChatsUserDetailOutputSerializer,
    ChatsUserCreateInputSerializer,
    ChatsUserUpdateInputSerializer,
    ChatsUserPartialUpdateInputSerializer,
    ChatsUserFilterOutputSerializer,
    ChatsUserFilterInputSerializer,
    ChatsUserStatsOutputSerializer,
)
from .serializers.chats_serializers import (
    ChatsChatSearchOutputSerializer,
    ChatsChatListOutputSerializer,
    ChatsChatDetailOutputSerializer,
    ChatsChatCreateInputSerializer,
    ChatsChatUpdateInputSerializer,
    ChatsChatPartialUpdateInputSerializer,
    ChatsChatFilterOutputSerializer,
    ChatsChatFilterInputSerializer,
    ChatsChatStatsOutputSerializer,
)
from .serializers.messages_serializers import (
    ChatsMessageSearchOutputSerializer,
    ChatsMessageListOutputSerializer,
    ChatsMessageDetailOutputSerializer,
    ChatsMessageCreateInputSerializer,
    ChatsMessageUpdateInputSerializer,
    ChatsMessagePartialUpdateInputSerializer,
    ChatsMessageFilterOutputSerializer,
    ChatsMessageFilterInputSerializer,
    ChatsMessageStatsOutputSerializer,
)
from .serializers.profile_serializers import (
    ChatsProfileOutputSerializer,
)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "ChatsInlineUserListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsUserListOutputSerializer(many=True),
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
    us = ChatsUserListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    responses={
        200: ChatsUserDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def users_detail(request: Request, pk: int) -> Response:
    u = ChatsUserDetailOutputSerializer(get_object_or_404(User, pk=pk))
    return Response(u.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "ChatsInlineUserSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsUserSearchOutputSerializer(many=True),
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
            Q(id__icontains=q) | Q(username__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = ChatsUserSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    request=ChatsUserCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def users_create(request: Request) -> Response:
    u = ChatsUserCreateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.create(**u.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=ChatsUserUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def users_update(request: Request, pk: int) -> Response:
    u = ChatsUserUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=ChatsUserPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def users_partial_update(request: Request, pk: int) -> Response:
    u = ChatsUserPartialUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "ChatsInlineUserFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsUserFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="username", description="Filter by username", type=str),
    ],
)
@api_view(["GET"])
def users_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = ChatsUserFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = User.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("username")) is not None:
        queryset = queryset.filter(username=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = ChatsUserFilterOutputSerializer(page, many=True)
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
            "ChatsInlineChatListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsChatListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def chats_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(
        Chat.objects.prefetch_related("users").order_by("id").all(), request
    )
    cs = ChatsChatListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={
        200: ChatsChatDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def chats_detail(request: Request, pk: int) -> Response:
    c = ChatsChatDetailOutputSerializer(get_object_or_404(Chat, pk=pk))
    return Response(c.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "ChatsInlineChatSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsChatSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def chats_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Chat.objects.order_by("id")
    else:
        queryset = Chat.objects.filter(
            Q(id__icontains=q) | Q(name__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = ChatsChatSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    request=ChatsChatCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def chats_create(request: Request) -> Response:
    c = ChatsChatCreateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    users = body.pop("users", [])
    chat = Chat.objects.create(**body)
    if users:
        chat.users.set(users)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=ChatsChatUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def chats_update(request: Request, pk: int) -> Response:
    c = ChatsChatUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    users = body.pop("users", None)
    Chat.objects.filter(pk=pk).update(**body)
    if users is not None:
        chat = Chat.objects.get(pk=pk)
        chat.users.set(users)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=ChatsChatPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def chats_partial_update(request: Request, pk: int) -> Response:
    c = ChatsChatPartialUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    users = body.pop("users", None)
    Chat.objects.filter(pk=pk).update(**body)
    if users is not None:
        chat = Chat.objects.get(pk=pk)
        chat.users.set(users)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "ChatsInlineChatFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsChatFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="name", description="Filter by name", type=str),
    ],
)
@api_view(["GET"])
def chats_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = ChatsChatFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Chat.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = ChatsChatFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def chats_delete(request: Request, pk: int) -> Response:
    Chat.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "ChatsInlineMessageListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsMessageListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def messages_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Message.objects.order_by("id").all(), request)
    ms = ChatsMessageListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ms.data)


@extend_schema(
    responses={
        200: ChatsMessageDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def messages_detail(request: Request, pk: int) -> Response:
    m = ChatsMessageDetailOutputSerializer(get_object_or_404(Message, pk=pk))
    return Response(m.data)


@extend_schema(
    responses={
        200: inline_serializer(
            "ChatsInlineMessageSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsMessageSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def messages_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Message.objects.order_by("id")
    else:
        queryset = Message.objects.filter(
            Q(id__icontains=q)
            | Q(text__icontains=q)
            | Q(chat__id__icontains=q)
            | Q(author__id__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ms = ChatsMessageSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ms.data)


@extend_schema(
    request=ChatsMessageCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def messages_create(request: Request) -> Response:
    m = ChatsMessageCreateInputSerializer(data=request.data)
    m.is_valid(raise_exception=True)
    body = m.validated_data
    body["chat_id"] = body.pop("chat")
    body["author_id"] = body.pop("author")
    Message.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=ChatsMessageUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def messages_update(request: Request, pk: int) -> Response:
    m = ChatsMessageUpdateInputSerializer(data=request.data)
    m.is_valid(raise_exception=True)
    body = m.validated_data
    body["chat_id"] = body.pop("chat")
    body["author_id"] = body.pop("author")
    Message.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=ChatsMessagePartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def messages_partial_update(request: Request, pk: int) -> Response:
    m = ChatsMessagePartialUpdateInputSerializer(data=request.data)
    m.is_valid(raise_exception=True)
    body = m.validated_data
    if body.get("chat") is not None:
        body["chat_id"] = body.pop("chat")
    if body.get("author") is not None:
        body["author_id"] = body.pop("author")
    Message.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        200: inline_serializer(
            "ChatsInlineMessageFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ChatsMessageFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="chat", description="Filter by chat", type=int),
        OpenApiParameter(name="author", description="Filter by author", type=int),
    ],
)
@api_view(["GET"])
def messages_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = ChatsMessageFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Message.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("chat")) is not None:
        queryset = queryset.filter(chat=q)
    if (q := validated_data.get("author")) is not None:
        queryset = queryset.filter(author=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ms = ChatsMessageFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ms.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def messages_delete(request: Request, pk: int) -> Response:
    Message.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(responses={status.HTTP_200_OK: ChatsProfileOutputSerializer()})
@api_view(["GET"])
def profile(request: Request, pk: int) -> Response:
    user = get_object_or_404(
        User.objects.prefetch_related(
            "chat_set__users", "chat_set__message_set__author"
        ),
        id=pk,
    )

    profile_data = {
        "user_info": {
            "username": user.username,
            "created_at": user.created_at,
        },
        "chats": [
            {
                "id": chat.id,
                "name": chat.name,
                "created_at": chat.created_at,
                "users": [
                    {"id": u.id, "username": u.username} for u in chat.users.all()
                ],
                "messages": [
                    {
                        "id": msg.id,
                        "text": msg.text,
                        "created_at": msg.created_at,
                        "author": {
                            "id": msg.author_id,
                            "username": msg.author.username,
                        },
                    }
                    for msg in chat.message_set.all()
                ],
            }
            for chat in user.chat_set.all()
        ],
    }
    serializer = ChatsProfileOutputSerializer(profile_data)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: ChatsUserStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def users_stats(request: Request) -> Response:
    data = (
        User.objects.annotate(count_users=Count("id"))
        .values("count_users")
        .order_by("-count_users")
    )
    serializer = ChatsUserStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: ChatsChatStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def chats_stats(request: Request) -> Response:
    data = (
        Chat.objects.annotate(count_chats=Count("id"))
        .values("count_chats")
        .order_by("-count_chats")
    )
    serializer = ChatsChatStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: ChatsMessageStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def messages_stats(request: Request) -> Response:
    data = (
        Message.objects.values("chat_id")
        .annotate(count_messages=Count("id"))
        .order_by("-count_messages")
    )
    serializer = ChatsMessageStatsOutputSerializer(data, many=True)
    return Response(serializer.data)
