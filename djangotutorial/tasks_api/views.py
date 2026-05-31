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
from .models import Status, Priority, Category, Role, Group, Project, User, Task, News, Comment
from .serializers.status_serializers import (
    TasksStatusSearchOutputSerializer,
    TasksStatusListOutputSerializer,
    TasksStatusDetailOutputSerializer,
    TasksStatusCreateInputSerializer,
    TasksStatusUpdateInputSerializer,
    TasksStatusPartialUpdateInputSerializer,
    TasksStatusFilterOutputSerializer,
    TasksStatusFilterInputSerializer,
    TasksStatusStatsOutputSerializer,
)
from .serializers.priority_serializers import (
    TasksPrioritySearchOutputSerializer,
    TasksPriorityListOutputSerializer,
    TasksPriorityDetailOutputSerializer,
    TasksPriorityCreateInputSerializer,
    TasksPriorityUpdateInputSerializer,
    TasksPriorityPartialUpdateInputSerializer,
    TasksPriorityFilterOutputSerializer,
    TasksPriorityFilterInputSerializer,
    TasksPriorityStatsOutputSerializer,
)
from .serializers.category_serializers import (
    TasksCategorySearchOutputSerializer,
    TasksCategoryListOutputSerializer,
    TasksCategoryDetailOutputSerializer,
    TasksCategoryCreateInputSerializer,
    TasksCategoryUpdateInputSerializer,
    TasksCategoryPartialUpdateInputSerializer,
    TasksCategoryFilterOutputSerializer,
    TasksCategoryFilterInputSerializer,
    TasksCategoryStatsOutputSerializer,
)
from .serializers.role_serializers import (
    TasksRoleSearchOutputSerializer,
    TasksRoleListOutputSerializer,
    TasksRoleDetailOutputSerializer,
    TasksRoleCreateInputSerializer,
    TasksRoleUpdateInputSerializer,
    TasksRolePartialUpdateInputSerializer,
    TasksRoleFilterOutputSerializer,
    TasksRoleFilterInputSerializer,
    TasksRoleStatsOutputSerializer,
)
from .serializers.group_serializers import (
    TasksGroupSearchOutputSerializer,
    TasksGroupListOutputSerializer,
    TasksGroupDetailOutputSerializer,
    TasksGroupCreateInputSerializer,
    TasksGroupUpdateInputSerializer,
    TasksGroupPartialUpdateInputSerializer,
    TasksGroupFilterOutputSerializer,
    TasksGroupFilterInputSerializer,
    TasksGroupStatsOutputSerializer,
)
from .serializers.project_serializers import (
    TasksProjectSearchOutputSerializer,
    TasksProjectListOutputSerializer,
    TasksProjectDetailOutputSerializer,
    TasksProjectCreateInputSerializer,
    TasksProjectUpdateInputSerializer,
    TasksProjectPartialUpdateInputSerializer,
    TasksProjectFilterOutputSerializer,
    TasksProjectFilterInputSerializer,
    TasksProjectStatsOutputSerializer,
)
from .serializers.users_serializers import (
    TasksUserSearchOutputSerializer,
    TasksUserListOutputSerializer,
    TasksUserDetailOutputSerializer,
    TasksUserCreateInputSerializer,
    TasksUserUpdateInputSerializer,
    TasksUserPartialUpdateInputSerializer,
    TasksUserFilterOutputSerializer,
    TasksUserFilterInputSerializer,
    TasksUserStatsOutputSerializer,
)
from .serializers.task_serializers import (
    TasksTaskSearchOutputSerializer,
    TasksTaskListOutputSerializer,
    TasksTaskDetailOutputSerializer,
    TasksTaskCreateInputSerializer,
    TasksTaskUpdateInputSerializer,
    TasksTaskPartialUpdateInputSerializer,
    TasksTaskFilterOutputSerializer,
    TasksTaskFilterInputSerializer,
    TasksTaskStatsOutputSerializer,
)
from .serializers.news_serializers import (
    TasksNewsSearchOutputSerializer,
    TasksNewsListOutputSerializer,
    TasksNewsDetailOutputSerializer,
    TasksNewsCreateInputSerializer,
    TasksNewsUpdateInputSerializer,
    TasksNewsPartialUpdateInputSerializer,
    TasksNewsFilterOutputSerializer,
    TasksNewsFilterInputSerializer,
    TasksNewsStatsOutputSerializer,
)
from .serializers.comment_serializers import (
    TasksCommentSearchOutputSerializer,
    TasksCommentListOutputSerializer,
    TasksCommentDetailOutputSerializer,
    TasksCommentCreateInputSerializer,
    TasksCommentUpdateInputSerializer,
    TasksCommentPartialUpdateInputSerializer,
    TasksCommentFilterOutputSerializer,
    TasksCommentFilterInputSerializer,
    TasksCommentStatsOutputSerializer,
)
from .serializers.profile_serializers import TasksProfileOutputSerializer


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineStatusListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksStatusListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def statuses_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Status.objects.order_by("id").all(), request)
    ss = TasksStatusListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ss.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksStatusDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def statuses_detail(request: Request, pk: int) -> Response:
    s = TasksStatusDetailOutputSerializer(get_object_or_404(Status, pk=pk))
    return Response(s.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineStatusSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksStatusSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def statuses_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Status.objects.order_by("id")
    else:
        queryset = Status.objects.filter(
            Q(id__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ss = TasksStatusSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ss.data)


@extend_schema(
    request=TasksStatusCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def statuses_create(request: Request) -> Response:
    s = TasksStatusCreateInputSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    Status.objects.create(**s.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksStatusUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def statuses_update(request: Request, pk: int) -> Response:
    s = TasksStatusUpdateInputSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    Status.objects.filter(pk=pk).update(**s.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksStatusPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def statuses_partial_update(request: Request, pk: int) -> Response:
    s = TasksStatusPartialUpdateInputSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    Status.objects.filter(pk=pk).update(**s.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineStatusFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksStatusFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="name", description="Filter by name", type=str),
        OpenApiParameter(name="is_close", description="Filter by is_close", type=bool),
    ],
)
@api_view(["GET"])
def statuses_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksStatusFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Status.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)
    if (q := validated_data.get("is_close")) is not None:
        queryset = queryset.filter(is_close=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ss = TasksStatusFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ss.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def statuses_delete(request: Request, pk: int) -> Response:
    Status.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlinePriorityListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksPriorityListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def priorities_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Priority.objects.order_by("id").all(), request)
    ps = TasksPriorityListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksPriorityDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def priorities_detail(request: Request, pk: int) -> Response:
    p = TasksPriorityDetailOutputSerializer(get_object_or_404(Priority, pk=pk))
    return Response(p.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlinePrioritySearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksPrioritySearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def priorities_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Priority.objects.order_by("id")
    else:
        queryset = Priority.objects.filter(
            Q(id__icontains=q) | Q(name__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = TasksPrioritySearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    request=TasksPriorityCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def priorities_create(request: Request) -> Response:
    p = TasksPriorityCreateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Priority.objects.create(**p.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksPriorityUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def priorities_update(request: Request, pk: int) -> Response:
    p = TasksPriorityUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Priority.objects.filter(pk=pk).update(**p.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksPriorityPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def priorities_partial_update(request: Request, pk: int) -> Response:
    p = TasksPriorityPartialUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Priority.objects.filter(pk=pk).update(**p.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlinePriorityFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksPriorityFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="name", description="Filter by name", type=str),
        OpenApiParameter(name="active", description="Filter by active", type=bool),
    ],
)
@api_view(["GET"])
def priorities_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksPriorityFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Priority.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)
    if (q := validated_data.get("active")) is not None:
        queryset = queryset.filter(active=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = TasksPriorityFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def priorities_delete(request: Request, pk: int) -> Response:
    Priority.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineCategoryListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksCategoryListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def categories_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Category.objects.order_by("id").all(), request)
    cs = TasksCategoryListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksCategoryDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def categories_detail(request: Request, pk: int) -> Response:
    c = TasksCategoryDetailOutputSerializer(get_object_or_404(Category, pk=pk))
    return Response(c.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineCategorySearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksCategorySearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def categories_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Category.objects.order_by("id")
    else:
        queryset = Category.objects.filter(
            Q(id__icontains=q) | Q(name__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = TasksCategorySearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    request=TasksCategoryCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def categories_create(request: Request) -> Response:
    c = TasksCategoryCreateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    Category.objects.create(**c.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksCategoryUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def categories_update(request: Request, pk: int) -> Response:
    c = TasksCategoryUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    Category.objects.filter(pk=pk).update(**c.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksCategoryPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def categories_partial_update(request: Request, pk: int) -> Response:
    c = TasksCategoryPartialUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    Category.objects.filter(pk=pk).update(**c.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineCategoryFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksCategoryFilterOutputSerializer(many=True),
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
def categories_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksCategoryFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Category.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = TasksCategoryFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def categories_delete(request: Request, pk: int) -> Response:
    Category.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineRoleListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksRoleListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def roles_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Role.objects.order_by("id").all(), request)
    rs = TasksRoleListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksRoleDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def roles_detail(request: Request, pk: int) -> Response:
    r = TasksRoleDetailOutputSerializer(get_object_or_404(Role, pk=pk))
    return Response(r.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineRoleSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksRoleSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def roles_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Role.objects.order_by("id")
    else:
        queryset = Role.objects.filter(
            Q(id__icontains=q) | Q(name__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    rs = TasksRoleSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@extend_schema(
    request=TasksRoleCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def roles_create(request: Request) -> Response:
    r = TasksRoleCreateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    Role.objects.create(**r.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksRoleUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def roles_update(request: Request, pk: int) -> Response:
    r = TasksRoleUpdateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    Role.objects.filter(pk=pk).update(**r.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksRolePartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def roles_partial_update(request: Request, pk: int) -> Response:
    r = TasksRolePartialUpdateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    Role.objects.filter(pk=pk).update(**r.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineRoleFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksRoleFilterOutputSerializer(many=True),
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
def roles_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksRoleFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Role.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    rs = TasksRoleFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def roles_delete(request: Request, pk: int) -> Response:
    Role.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineGroupListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksGroupListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def groups_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Group.objects.order_by("id").all(), request)
    gs = TasksGroupListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(gs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksGroupDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def groups_detail(request: Request, pk: int) -> Response:
    g = TasksGroupDetailOutputSerializer(get_object_or_404(Group, pk=pk))
    return Response(g.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineGroupSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksGroupSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def groups_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Group.objects.order_by("id")
    else:
        queryset = Group.objects.filter(
            Q(id__icontains=q) | Q(name__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    gs = TasksGroupSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(gs.data)


@extend_schema(
    request=TasksGroupCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def groups_create(request: Request) -> Response:
    g = TasksGroupCreateInputSerializer(data=request.data)
    g.is_valid(raise_exception=True)
    Group.objects.create(**g.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksGroupUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def groups_update(request: Request, pk: int) -> Response:
    g = TasksGroupUpdateInputSerializer(data=request.data)
    g.is_valid(raise_exception=True)
    Group.objects.filter(pk=pk).update(**g.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksGroupPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def groups_partial_update(request: Request, pk: int) -> Response:
    g = TasksGroupPartialUpdateInputSerializer(data=request.data)
    g.is_valid(raise_exception=True)
    Group.objects.filter(pk=pk).update(**g.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineGroupFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksGroupFilterOutputSerializer(many=True),
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
def groups_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksGroupFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Group.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    gs = TasksGroupFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(gs.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def groups_delete(request: Request, pk: int) -> Response:
    Group.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineProjectListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksProjectListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def projects_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Project.objects.order_by("id").all(), request)
    ps = TasksProjectListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksProjectDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def projects_detail(request: Request, pk: int) -> Response:
    p = TasksProjectDetailOutputSerializer(get_object_or_404(Project, pk=pk))
    return Response(p.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineProjectSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksProjectSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def projects_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Project.objects.order_by("id")
    else:
        queryset = Project.objects.filter(
            Q(id__icontains=q) | Q(identifier__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = TasksProjectSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    request=TasksProjectCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def projects_create(request: Request) -> Response:
    p = TasksProjectCreateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    parent = body.pop("parent", None)
    if parent is not None:
        body["parent_id"] = parent
    Project.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksProjectUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def projects_update(request: Request, pk: int) -> Response:
    p = TasksProjectUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    parent = body.pop("parent", None)
    if parent is not None:
        body["parent_id"] = parent
    Project.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksProjectPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def projects_partial_update(request: Request, pk: int) -> Response:
    p = TasksProjectPartialUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    if body.get("parent") is not None:
        body["parent_id"] = body.pop("parent")
    Project.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineProjectFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksProjectFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="identifier", description="Filter by identifier", type=str),
        OpenApiParameter(name="name", description="Filter by name", type=str),
        OpenApiParameter(name="is_public", description="Filter by is_public", type=bool),
    ],
)
@api_view(["GET"])
def projects_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksProjectFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Project.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("identifier")) is not None:
        queryset = queryset.filter(identifier=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)
    if (q := validated_data.get("is_public")) is not None:
        queryset = queryset.filter(is_public=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = TasksProjectFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def projects_delete(request: Request, pk: int) -> Response:
    Project.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineUserListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksUserListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def tasks_users_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(User.objects.order_by("id").all(), request)
    us = TasksUserListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksUserDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def tasks_users_detail(request: Request, pk: int) -> Response:
    u = TasksUserDetailOutputSerializer(get_object_or_404(User, pk=pk))
    return Response(u.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineUserSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksUserSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def tasks_users_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = User.objects.order_by("id")
    else:
        queryset = User.objects.filter(
            Q(id__icontains=q)
            | Q(login__icontains=q)
            | Q(firstname__icontains=q)
            | Q(lastname__icontains=q)
            | Q(mail__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = TasksUserSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    request=TasksUserCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def tasks_users_create(request: Request) -> Response:
    u = TasksUserCreateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    body = u.validated_data
    body["role_id"] = body.pop("role")
    body["group_id"] = body.pop("group")
    User.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksUserUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def tasks_users_update(request: Request, pk: int) -> Response:
    u = TasksUserUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    body = u.validated_data
    body["role_id"] = body.pop("role")
    body["group_id"] = body.pop("group")
    User.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksUserPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def tasks_users_partial_update(request: Request, pk: int) -> Response:
    u = TasksUserPartialUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    body = u.validated_data
    if body.get("role") is not None:
        body["role_id"] = body.pop("role")
    if body.get("group") is not None:
        body["group_id"] = body.pop("group")
    User.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineUserFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksUserFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="login", description="Filter by login", type=str),
        OpenApiParameter(name="admin", description="Filter by admin", type=bool),
        OpenApiParameter(name="firstname", description="Filter by firstname", type=str),
        OpenApiParameter(name="lastname", description="Filter by lastname", type=str),
        OpenApiParameter(name="role", description="Filter by role", type=int),
        OpenApiParameter(name="group", description="Filter by group", type=int),
    ],
)
@api_view(["GET"])
def tasks_users_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksUserFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = User.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("login")) is not None:
        queryset = queryset.filter(login=q)
    if (q := validated_data.get("admin")) is not None:
        queryset = queryset.filter(admin=q)
    if (q := validated_data.get("firstname")) is not None:
        queryset = queryset.filter(firstname=q)
    if (q := validated_data.get("lastname")) is not None:
        queryset = queryset.filter(lastname=q)
    if (q := validated_data.get("role")) is not None:
        queryset = queryset.filter(role=q)
    if (q := validated_data.get("group")) is not None:
        queryset = queryset.filter(group=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = TasksUserFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def tasks_users_delete(request: Request, pk: int) -> Response:
    User.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineTaskListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksTaskListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def tasks_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Task.objects.order_by("id").all(), request)
    ts = TasksTaskListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksTaskDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def tasks_detail(request: Request, pk: int) -> Response:
    t = TasksTaskDetailOutputSerializer(get_object_or_404(Task, pk=pk))
    return Response(t.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineTaskSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksTaskSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def tasks_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Task.objects.order_by("id")
    else:
        queryset = Task.objects.filter(
            Q(id__icontains=q)
            | Q(subject__icontains=q)
            | Q(description__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ts = TasksTaskSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@extend_schema(
    request=TasksTaskCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def tasks_create(request: Request) -> Response:
    t = TasksTaskCreateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    if body.get("parent") is not None:
        body["parent_id"] = body.pop("parent")
    body["category_id"] = body.pop("category")
    body["assigned_to_id"] = body.pop("assigned_to")
    body["author_id"] = body.pop("author")
    body["priority_id"] = body.pop("priority")
    body["status_id"] = body.pop("status")
    body["project_id"] = body.pop("project")
    Task.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksTaskUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def tasks_update(request: Request, pk: int) -> Response:
    t = TasksTaskUpdateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    if body.get("parent") is not None:
        body["parent_id"] = body.pop("parent")
    body["category_id"] = body.pop("category")
    body["assigned_to_id"] = body.pop("assigned_to")
    body["author_id"] = body.pop("author")
    body["priority_id"] = body.pop("priority")
    body["status_id"] = body.pop("status")
    body["project_id"] = body.pop("project")
    Task.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksTaskPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def tasks_partial_update(request: Request, pk: int) -> Response:
    t = TasksTaskPartialUpdateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    if body.get("parent") is not None:
        body["parent_id"] = body.pop("parent")
    if body.get("category") is not None:
        body["category_id"] = body.pop("category")
    if body.get("assigned_to") is not None:
        body["assigned_to_id"] = body.pop("assigned_to")
    if body.get("author") is not None:
        body["author_id"] = body.pop("author")
    if body.get("priority") is not None:
        body["priority_id"] = body.pop("priority")
    if body.get("status") is not None:
        body["status_id"] = body.pop("status")
    if body.get("project") is not None:
        body["project_id"] = body.pop("project")
    Task.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineTaskFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksTaskFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="subject", description="Filter by subject", type=str),
        OpenApiParameter(name="is_private", description="Filter by is_private", type=bool),
        OpenApiParameter(name="category", description="Filter by category", type=int),
        OpenApiParameter(name="assigned_to", description="Filter by assigned_to", type=int),
        OpenApiParameter(name="author", description="Filter by author", type=int),
        OpenApiParameter(name="priority", description="Filter by priority", type=int),
        OpenApiParameter(name="status", description="Filter by status", type=int),
        OpenApiParameter(name="project", description="Filter by project", type=int),
    ],
)
@api_view(["GET"])
def tasks_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksTaskFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Task.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("subject")) is not None:
        queryset = queryset.filter(subject=q)
    if (q := validated_data.get("is_private")) is not None:
        queryset = queryset.filter(is_private=q)
    if (q := validated_data.get("category")) is not None:
        queryset = queryset.filter(category=q)
    if (q := validated_data.get("assigned_to")) is not None:
        queryset = queryset.filter(assigned_to=q)
    if (q := validated_data.get("author")) is not None:
        queryset = queryset.filter(author=q)
    if (q := validated_data.get("priority")) is not None:
        queryset = queryset.filter(priority=q)
    if (q := validated_data.get("status")) is not None:
        queryset = queryset.filter(status=q)
    if (q := validated_data.get("project")) is not None:
        queryset = queryset.filter(project=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ts = TasksTaskFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def tasks_delete(request: Request, pk: int) -> Response:
    Task.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineNewsListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksNewsListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def news_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(News.objects.order_by("id").all(), request)
    ns = TasksNewsListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ns.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksNewsDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def news_detail(request: Request, pk: int) -> Response:
    n = TasksNewsDetailOutputSerializer(get_object_or_404(News, pk=pk))
    return Response(n.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineNewsSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksNewsSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def news_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = News.objects.order_by("id")
    else:
        queryset = News.objects.filter(
            Q(id__icontains=q)
            | Q(title__icontains=q)
            | Q(summary__icontains=q)
            | Q(description__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ns = TasksNewsSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ns.data)


@extend_schema(
    request=TasksNewsCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def news_create(request: Request) -> Response:
    n = TasksNewsCreateInputSerializer(data=request.data)
    n.is_valid(raise_exception=True)
    body = n.validated_data
    body["project_id"] = body.pop("project")
    body["author_id"] = body.pop("author")
    News.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksNewsUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def news_update(request: Request, pk: int) -> Response:
    n = TasksNewsUpdateInputSerializer(data=request.data)
    n.is_valid(raise_exception=True)
    body = n.validated_data
    body["project_id"] = body.pop("project")
    body["author_id"] = body.pop("author")
    News.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksNewsPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def news_partial_update(request: Request, pk: int) -> Response:
    n = TasksNewsPartialUpdateInputSerializer(data=request.data)
    n.is_valid(raise_exception=True)
    body = n.validated_data
    if body.get("project") is not None:
        body["project_id"] = body.pop("project")
    if body.get("author") is not None:
        body["author_id"] = body.pop("author")
    News.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineNewsFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksNewsFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(name="project", description="Filter by project", type=int),
        OpenApiParameter(name="author", description="Filter by author", type=int),
    ],
)
@api_view(["GET"])
def news_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksNewsFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = News.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("title")) is not None:
        queryset = queryset.filter(title=q)
    if (q := validated_data.get("project")) is not None:
        queryset = queryset.filter(project=q)
    if (q := validated_data.get("author")) is not None:
        queryset = queryset.filter(author=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ns = TasksNewsFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ns.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def news_delete(request: Request, pk: int) -> Response:
    News.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineCommentListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksCommentListOutputSerializer(many=True),
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
    page = paginator.paginate_queryset(Comment.objects.order_by("id").all(), request)
    cs = TasksCommentListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: TasksCommentDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def comments_detail(request: Request, pk: int) -> Response:
    c = TasksCommentDetailOutputSerializer(get_object_or_404(Comment, pk=pk))
    return Response(c.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineCommentSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksCommentSearchOutputSerializer(many=True),
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
            Q(id__icontains=q) | Q(content__icontains=q)
        ).order_by("id")

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = TasksCommentSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    request=TasksCommentCreateInputSerializer,
    responses={status.HTTP_201_CREATED: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def comments_create(request: Request) -> Response:
    c = TasksCommentCreateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["author_id"] = body.pop("author")
    body["some_news_id"] = body.pop("some_news")
    Comment.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=TasksCommentUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def comments_update(request: Request, pk: int) -> Response:
    c = TasksCommentUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["author_id"] = body.pop("author")
    body["some_news_id"] = body.pop("some_news")
    Comment.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=TasksCommentPartialUpdateInputSerializer,
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def comments_partial_update(request: Request, pk: int) -> Response:
    c = TasksCommentPartialUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    if body.get("author") is not None:
        body["author_id"] = body.pop("author")
    if body.get("some_news") is not None:
        body["some_news_id"] = body.pop("some_news")
    Comment.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "TasksInlineCommentFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": TasksCommentFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="author", description="Filter by author", type=int),
        OpenApiParameter(name="some_news", description="Filter by some_news", type=int),
    ],
)
@api_view(["GET"])
def comments_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = TasksCommentFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data

    queryset = Comment.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("author")) is not None:
        queryset = queryset.filter(author=q)
    if (q := validated_data.get("some_news")) is not None:
        queryset = queryset.filter(some_news=q)

    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = TasksCommentFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={status.HTTP_200_OK: None},
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["DELETE"])
@permission_classes([TokenPermission])
def comments_delete(request: Request, pk: int) -> Response:
    Comment.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(responses={status.HTTP_200_OK: TasksProfileOutputSerializer()})
@api_view(["GET"])
def profile(request: Request, pk: int) -> Response:
    user = get_object_or_404(
        User.objects.prefetch_related(
            "assigned_tasks", "news_set", "comment_set"
        ),
        id=pk,
    )

    profile_data = {
        "user_info": {
            "login": user.login,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "mail": user.mail,
            "admin": user.admin,
        },
        "tasks": [
            {
                "id": t.id,
                "subject": t.subject,
                "description": t.description,
                "done_percent": t.done_percent,
            }
            for t in user.assigned_tasks.all()
        ],
        "news": [
            {
                "id": n.id,
                "title": n.title,
                "summary": n.summary,
            }
            for n in user.news_set.all()
        ],
        "comments": [
            {
                "id": c.id,
                "content": c.content,
                "created_on": c.created_on,
            }
            for c in user.comment_set.all()
        ],
    }
    serializer = TasksProfileOutputSerializer(profile_data)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksStatusStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def statuses_stats(request: Request) -> Response:
    data = (
        Status.objects.annotate(count_statuses=Count("id"))
        .values("count_statuses")
        .order_by("-count_statuses")
    )
    serializer = TasksStatusStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksPriorityStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def priorities_stats(request: Request) -> Response:
    data = (
        Priority.objects.annotate(count_priorities=Count("id"))
        .values("count_priorities")
        .order_by("-count_priorities")
    )
    serializer = TasksPriorityStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksCategoryStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def categories_stats(request: Request) -> Response:
    data = (
        Category.objects.annotate(count_categories=Count("id"))
        .values("count_categories")
        .order_by("-count_categories")
    )
    serializer = TasksCategoryStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksRoleStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def roles_stats(request: Request) -> Response:
    data = (
        Role.objects.annotate(count_roles=Count("id"))
        .values("count_roles")
        .order_by("-count_roles")
    )
    serializer = TasksRoleStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksGroupStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def groups_stats(request: Request) -> Response:
    data = (
        Group.objects.annotate(count_groups=Count("id"))
        .values("count_groups")
        .order_by("-count_groups")
    )
    serializer = TasksGroupStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksProjectStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def projects_stats(request: Request) -> Response:
    data = (
        Project.objects.annotate(count_projects=Count("id"))
        .values("count_projects")
        .order_by("-count_projects")
    )
    serializer = TasksProjectStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksUserStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def tasks_users_stats(request: Request) -> Response:
    data = (
        User.objects.values("role_id")
        .annotate(count_users=Count("id"))
        .order_by("-count_users")
    )
    serializer = TasksUserStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksTaskStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def tasks_stats(request: Request) -> Response:
    data = (
        Task.objects.values("project_id")
        .annotate(count_tasks=Count("id"))
        .order_by("-count_tasks")
    )
    serializer = TasksTaskStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksNewsStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def news_stats(request: Request) -> Response:
    data = (
        News.objects.values("project_id")
        .annotate(count_news=Count("id"))
        .order_by("-count_news")
    )
    serializer = TasksNewsStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TasksCommentStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def comments_stats(request: Request) -> Response:
    data = (
        Comment.objects.values("some_news_id")
        .annotate(count_comments=Count("id"))
        .order_by("-count_comments")
    )
    serializer = TasksCommentStatsOutputSerializer(data, many=True)
    return Response(serializer.data)
