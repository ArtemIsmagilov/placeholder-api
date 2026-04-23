from django.shortcuts import get_object_or_404
from django.db.models import Q, F, Count, Sum, Avg, Max, Min
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiParameter

from dummy_api.models import (
    User,
    Todo,
    Recipe,
    Quote,
    Product,
    Review,
    Post,
    Comment,
    Cart,
)
from dummy_api.serializers.users_serializers import (
    UserListOutputSerializer,
    UserDetailOutputSerializer,
    UserSearchOutputSerializer,
    UserCreateInputSerializer,
    UserUpdateInputSerializer,
    UserPartialUpdateInputSerializer,
    UserFilterOutputSerializer,
    UserFilterInputSerializer,
    UsersStatsOutputSerializer,
)
from dummy_api.serializers.todos_serializers import (
    TodoListOutputSerializer,
    TodoDetailOutputSerializer,
    TodoSearchOutputSerializer,
    TodoCreateInputSerializer,
    TodoUpdateInputSerializer,
    TodoPartialUpdateInputSerializer,
    TodoFilterOutputSerializer,
    TodoFilterInputSerializer,
    TodosStatsOutputSerializer,
)
from dummy_api.serializers.recipes_serializers import (
    RecipeListOutputSerializer,
    RecipeDetailOutputSerializer,
    RecipeSearchOutputSerializer,
    RecipeCreateInputSerializer,
    RecipeUpdateInputSerializer,
    RecipePartialUpdateInputSerializer,
    RecipeFilterOutputSerializer,
    RecipeFilterInputSerializer,
    RecipesStatsOutputSerializer,
)
from dummy_api.serializers.quotes_serializers import (
    QuoteListOutputSerializer,
    QuoteDetailOutputSerializer,
    QuoteSearchOutputSerializer,
    QuoteCreateInputSerializer,
    QuoteUpdateInputSerializer,
    QuotePartialUpdateInputSerializer,
    QuoteFilterOutputSerializer,
    QuoteFilterInputSerializer,
    QuotesStatsOutputSerializer,
)
from dummy_api.serializers.products_serializers import (
    ProductListOutputSerializer,
    ProductDetailOutputSerializer,
    ProductSearchOutputSerializer,
    ProductCreateInputSerializer,
    ProductUpdateInputSerializer,
    ProductPartialUpdateInputSerializer,
    ProductFilterOutputSerializer,
    ProductFilterInputSerializer,
    ProductsStatsOutputSerializer,
)
from dummy_api.serializers.reviews_serializers import (
    ReviewListOutputSerializer,
    ReviewDetailOutputSerializer,
    ReviewSearchOutputSerializer,
    ReviewCreateInputSerializer,
    ReviewUpdateInputSerializer,
    ReviewPartialUpdateInputSerializer,
    ReviewFilterOutputSerializer,
    ReviewFilterInputSerializer,
    ReviewsStatsOutputSerializer,
)
from dummy_api.serializers.posts_serializers import (
    PostListOutputSerializer,
    PostDetailOutputSerializer,
    PostSearchOutputSerializer,
    PostCreateInputSerializer,
    PostUpdateInputSerializer,
    PostPartialUpdateInputSerializer,
    PostFilterOutputSerializer,
    PostFilterInputSerializer,
    PostsStatsOutputSerializer,
)
from dummy_api.serializers.comments_serializers import (
    CommentListOutputSerializer,
    CommentDetailOutputSerializer,
    CommentSearchOutputSerializer,
    CommentCreateInputSerializer,
    CommentUpdateInputSerializer,
    CommentPartialUpdateInputSerializer,
    CommentFilterOutputSerializer,
    CommentFilterInputSerializer,
    CommentsStatsOutputSerializer,
)
from dummy_api.serializers.carts_serializers import (
    CartListOutputSerializer,
    CartDetailOutputSerializer,
    CartSearchOutputSerializer,
    CartCreateInputSerializer,
    CartUpdateInputSerializer,
    CartPartialUpdateInputSerializer,
    CartFilterOutputSerializer,
    CartFilterInputSerializer,
    CartStatsOutputSerializer,
)
from dummy_api.serializers.profile_serializers import ProfileOutputSerializer
from mysite.base_permissions import TokenPermission


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
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
        status.HTTP_200_OK: UserDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def users_detail(request: Request, pk: int) -> Response:
    u = UserDetailOutputSerializer(get_object_or_404(User, pk=pk))
    return Response(u.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
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
        OpenApiParameter(name="q", description="Search query", type=str),
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
            | Q(first_name__icontains=q)
            | Q(last_name__icontains=q)
            | Q(maiden_name__icontains=q)
            | Q(age__icontains=q)
            | Q(gender__icontains=q)
            | Q(email__icontains=q)
            | Q(phone__icontains=q)
            | Q(username__icontains=q)
            | Q(password__icontains=q)
            | Q(birthday__icontains=q)
            | Q(image__icontains=q)
            | Q(blood_group__icontains=q)
            | Q(height__icontains=q)
            | Q(weight__icontains=q)
            | Q(eye_color__icontains=q)
            | Q(hair_color__icontains=q)
            | Q(hair_type__icontains=q)
            | Q(ip__icontains=q)
            | Q(address__icontains=q)
            | Q(city__icontains=q)
            | Q(state__icontains=q)
            | Q(state_code__icontains=q)
            | Q(postal_code__icontains=q)
            | Q(coordinates__icontains=q)
            | Q(country__icontains=q)
            | Q(mac_address__icontains=q)
            | Q(university__icontains=q)
            | Q(bank_card_expire__icontains=q)
            | Q(bank_card_number__icontains=q)
            | Q(bank_card_type__icontains=q)
            | Q(bank_currency__icontains=q)
            | Q(bank_iban__icontains=q)
            | Q(company_department__icontains=q)
            | Q(company_name__icontains=q)
            | Q(company_title__icontains=q)
            | Q(company_address__icontains=q)
            | Q(company_city__icontains=q)
            | Q(company_state__icontains=q)
            | Q(company_state_code__icontains=q)
            | Q(company_postal_code__icontains=q)
            | Q(company_coordinates__icontains=q)
            | Q(company_country__icontains=q)
            | Q(ein__icontains=q)
            | Q(ssn__icontains=q)
            | Q(user_agent__icontains=q)
            | Q(crypto_coint__icontains=q)
            | Q(crypto_wallet__icontains=q)
            | Q(crypto_network__icontains=q)
            | Q(role__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = UserSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@extend_schema(
    request=UserCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: UserCreateInputSerializer(),
    },
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
    responses={
        status.HTTP_200_OK: UserUpdateInputSerializer(),
    },
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
    responses={
        status.HTTP_200_OK: UserPartialUpdateInputSerializer(),
    },
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
        status.HTTP_200_OK: inline_serializer(
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
        OpenApiParameter(name=field, description=f"Filter by {field}", type=str)
        for field in [
            "id",
            "first_name",
            "last_name",
            "maiden_name",
            "age",
            "gender",
            "email",
            "phone",
            "username",
            "password",
            "birthday",
            "image",
            "blood_group",
            "height",
            "weight",
            "eye_color",
            "hair_color",
            "hair_type",
            "ip",
            "address",
            "city",
            "state",
            "state_code",
            "postal_code",
            "coordinates",
            "country",
            "mac_address",
            "university",
            "bank_card_expire",
            "bank_card_number",
            "bank_card_type",
            "bank_currency",
            "bank_iban",
            "company_department",
            "company_name",
            "company_title",
            "company_address",
            "company_city",
            "company_state",
            "company_state_code",
            "company_postal_code",
            "company_coordinates",
            "company_country",
            "ein",
            "ssn",
            "user_agent",
            "crypto_coint",
            "crypto_wallet",
            "crypto_network",
            "role",
        ]
    ]
    + [OpenApiParameter(name="page", description="Filter by page", type=int)],
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
    if (q := validated_data.get("first_name")) is not None:
        queryset = queryset.filter(first_name=q)
    if (q := validated_data.get("last_name")) is not None:
        queryset = queryset.filter(last_name=q)
    if (q := validated_data.get("maiden_name")) is not None:
        queryset = queryset.filter(maiden_name=q)
    if (q := validated_data.get("age")) is not None:
        queryset = queryset.filter(age=q)
    if (q := validated_data.get("gender")) is not None:
        queryset = queryset.filter(gender=q)
    if (q := validated_data.get("email")) is not None:
        queryset = queryset.filter(email=q)
    if (q := validated_data.get("phone")) is not None:
        queryset = queryset.filter(phone=q)
    if (q := validated_data.get("username")) is not None:
        queryset = queryset.filter(username=q)
    if (q := validated_data.get("password")) is not None:
        queryset = queryset.filter(password=q)
    if (q := validated_data.get("birthday")) is not None:
        queryset = queryset.filter(birthday=q)
    if (q := validated_data.get("image")) is not None:
        queryset = queryset.filter(image=q)
    if (q := validated_data.get("blood_group")) is not None:
        queryset = queryset.filter(blood_group=q)
    if (q := validated_data.get("height")) is not None:
        queryset = queryset.filter(height=q)
    if (q := validated_data.get("weight")) is not None:
        queryset = queryset.filter(weight=q)
    if (q := validated_data.get("eye_color")) is not None:
        queryset = queryset.filter(eye_color=q)
    if (q := validated_data.get("hair_color")) is not None:
        queryset = queryset.filter(hair_color=q)
    if (q := validated_data.get("hair_type")) is not None:
        queryset = queryset.filter(hair_type=q)
    if (q := validated_data.get("ip")) is not None:
        queryset = queryset.filter(ip=q)
    if (q := validated_data.get("address")) is not None:
        queryset = queryset.filter(address=q)
    if (q := validated_data.get("city")) is not None:
        queryset = queryset.filter(city=q)
    if (q := validated_data.get("state")) is not None:
        queryset = queryset.filter(state=q)
    if (q := validated_data.get("state_code")) is not None:
        queryset = queryset.filter(state_code=q)
    if (q := validated_data.get("postal_code")) is not None:
        queryset = queryset.filter(postal_code=q)
    if (q := validated_data.get("coordinates")) is not None:
        queryset = queryset.filter(coordinates=q)
    if (q := validated_data.get("country")) is not None:
        queryset = queryset.filter(country=q)
    if (q := validated_data.get("mac_address")) is not None:
        queryset = queryset.filter(mac_address=q)
    if (q := validated_data.get("university")) is not None:
        queryset = queryset.filter(university=q)
    if (q := validated_data.get("bank_card_expire")) is not None:
        queryset = queryset.filter(bank_card_expire=q)
    if (q := validated_data.get("bank_card_number")) is not None:
        queryset = queryset.filter(bank_card_number=q)
    if (q := validated_data.get("bank_card_type")) is not None:
        queryset = queryset.filter(bank_card_type=q)
    if (q := validated_data.get("bank_currency")) is not None:
        queryset = queryset.filter(bank_currency=q)
    if (q := validated_data.get("bank_iban")) is not None:
        queryset = queryset.filter(bank_iban=q)
    if (q := validated_data.get("company_department")) is not None:
        queryset = queryset.filter(company_department=q)
    if (q := validated_data.get("company_name")) is not None:
        queryset = queryset.filter(company_name=q)
    if (q := validated_data.get("company_title")) is not None:
        queryset = queryset.filter(company_title=q)
    if (q := validated_data.get("company_address")) is not None:
        queryset = queryset.filter(company_address=q)
    if (q := validated_data.get("company_city")) is not None:
        queryset = queryset.filter(company_city=q)
    if (q := validated_data.get("company_state")) is not None:
        queryset = queryset.filter(company_state=q)
    if (q := validated_data.get("company_state_code")) is not None:
        queryset = queryset.filter(company_state_code=q)
    if (q := validated_data.get("company_postal_code")) is not None:
        queryset = queryset.filter(company_postal_code=q)
    if (q := validated_data.get("company_coordinates")) is not None:
        queryset = queryset.filter(company_coordinates=q)
    if (q := validated_data.get("company_country")) is not None:
        queryset = queryset.filter(company_country=q)
    if (q := validated_data.get("ein")) is not None:
        queryset = queryset.filter(ein=q)
    if (q := validated_data.get("ssn")) is not None:
        queryset = queryset.filter(ssn=q)
    if (q := validated_data.get("user_agent")) is not None:
        queryset = queryset.filter(user_agent=q)
    if (q := validated_data.get("crypto_coint")) is not None:
        queryset = queryset.filter(crypto_coint=q)
    if (q := validated_data.get("crypto_wallet")) is not None:
        queryset = queryset.filter(crypto_wallet=q)
    if (q := validated_data.get("crypto_network")) is not None:
        queryset = queryset.filter(crypto_network=q)
    if (q := validated_data.get("role")) is not None:
        queryset = queryset.filter(role=q)
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = UserFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


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
def users_delete(request: Request, pk: int) -> Response:
    User.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
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
        status.HTTP_200_OK: TodoDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def todos_detail(request: Request, pk: int) -> Response:
    t = TodoDetailOutputSerializer(get_object_or_404(Todo, pk=pk))
    return Response(t.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
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
        OpenApiParameter(name="q", description="Search query", type=str),
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
            Q(id__icontains=q) | Q(title__icontains=q) | Q(completed__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ts = TodoSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@extend_schema(
    request=TodoCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: TodoCreateInputSerializer(),
    },
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
    responses={
        status.HTTP_200_OK: TodoUpdateInputSerializer(),
    },
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
    responses={
        status.HTTP_200_OK: TodoPartialUpdateInputSerializer(),
    },
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
        status.HTTP_200_OK: inline_serializer(
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
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(
            name="completed",
            description="Filter by completed",
            type=bool,
        ),
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
    responses={
        status.HTTP_200_OK: None,
    },
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
        status.HTTP_200_OK: inline_serializer(
            "InlineRecipeListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": RecipeListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def recipes_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Recipe.objects.order_by("id").all(), request)
    rs = RecipeListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: RecipeDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def recipes_detail(request: Request, pk: int) -> Response:
    r = RecipeDetailOutputSerializer(get_object_or_404(Recipe, pk=pk))
    return Response(r.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineRecipeSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": RecipeSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="q", description="Search query", type=str),
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def recipes_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Recipe.objects.order_by("id")
    else:
        queryset = Recipe.objects.filter(
            Q(id__icontains=q) | Q(name__icontains=q) | Q(cuisine__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    rs = RecipeSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@extend_schema(
    request=RecipeCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: RecipeCreateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def recipes_create(request: Request) -> Response:
    r = RecipeCreateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    body["user_id"] = body.pop("user")
    Recipe.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=RecipeUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: RecipeUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def recipes_update(request: Request, pk: int) -> Response:
    r = RecipeUpdateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    body["user_id"] = body.pop("user")
    Recipe.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=RecipePartialUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: RecipePartialUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def recipes_partial_update(request: Request, pk: int) -> Response:
    r = RecipePartialUpdateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Recipe.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineRecipeFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": RecipeFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="name", description="Filter by name", type=str),
        OpenApiParameter(
            name="ingredients",
            description="Filter by ingredients",
            type=str,
        ),
        OpenApiParameter(
            name="instructions",
            description="Filter by instructions",
            type=str,
        ),
        OpenApiParameter(
            name="prep_time_minutes",
            description="Filter by prep_time_minutes",
            type=int,
        ),
        OpenApiParameter(
            name="cook_time_minutes",
            description="Filter by cook_time_minutes",
            type=int,
        ),
        OpenApiParameter(name="servings", description="Filter by servings", type=int),
        OpenApiParameter(
            name="difficulty",
            description="Filter by difficulty",
            type=str,
        ),
        OpenApiParameter(name="cuisine", description="Filter by cuisine", type=str),
        OpenApiParameter(
            name="calories_per_serving",
            description="Filter by calories_per_serving",
            type=int,
        ),
        OpenApiParameter(name="tags", description="Filter by tags", type=str),
        OpenApiParameter(name="image", description="Filter by image", type=str),
        OpenApiParameter(name="rating", description="Filter by rating", type=float),
        OpenApiParameter(
            name="review_count",
            description="Filter by review_count",
            type=int,
        ),
        OpenApiParameter(
            name="meal_type",
            description="Filter by meal_type",
            type=str,
        ),
        OpenApiParameter(name="user", description="Filter by user", type=int),
    ],
)
@api_view(["GET"])
def recipes_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = RecipeFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data
    queryset = Recipe.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("name")) is not None:
        queryset = queryset.filter(name=q)
    if (q := validated_data.get("ingredients")) is not None:
        queryset = queryset.filter(ingredients=q)
    if (q := validated_data.get("instructions")) is not None:
        queryset = queryset.filter(instructions=q)
    if (q := validated_data.get("prep_time_minutes")) is not None:
        queryset = queryset.filter(prep_time_minutes=q)
    if (q := validated_data.get("cook_time_minutes")) is not None:
        queryset = queryset.filter(cook_time_minutes=q)
    if (q := validated_data.get("servings")) is not None:
        queryset = queryset.filter(servings=q)
    if (q := validated_data.get("difficulty")) is not None:
        queryset = queryset.filter(difficulty=q)
    if (q := validated_data.get("cuisine")) is not None:
        queryset = queryset.filter(cuisine=q)
    if (q := validated_data.get("calories_per_serving")) is not None:
        queryset = queryset.filter(calories_per_serving=q)
    if (q := validated_data.get("tags")) is not None:
        queryset = queryset.filter(tags=q)
    if (q := validated_data.get("image")) is not None:
        queryset = queryset.filter(image=q)
    if (q := validated_data.get("rating")) is not None:
        queryset = queryset.filter(rating=q)
    if (q := validated_data.get("review_count")) is not None:
        queryset = queryset.filter(review_count=q)
    if (q := validated_data.get("meal_type")) is not None:
        queryset = queryset.filter(meal_type=q)
    if (q := validated_data.get("user")) is not None:
        queryset = queryset.filter(user=q)
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    rs = RecipeFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


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
def recipes_delete(request: Request, pk: int) -> Response:
    Recipe.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineQuoteListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": QuoteListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def quotes_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Quote.objects.order_by("id").all(), request)
    qs = QuoteListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(qs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: QuoteDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def quotes_detail(request: Request, pk: int) -> Response:
    q = QuoteDetailOutputSerializer(get_object_or_404(Quote, pk=pk))
    return Response(q.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineQuoteSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": QuoteSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="q", description="Search query", type=str),
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def quotes_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Quote.objects.order_by("id")
    else:
        queryset = Quote.objects.filter(
            Q(id__icontains=q) | Q(title__icontains=q) | Q(author__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    qs = QuoteSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(qs.data)


@extend_schema(
    request=QuoteCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: QuoteCreateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def quotes_create(request: Request) -> Response:
    q = QuoteCreateInputSerializer(data=request.data)
    q.is_valid(raise_exception=True)
    Quote.objects.create(**q.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=QuoteUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: QuoteUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def quotes_update(request: Request, pk: int) -> Response:
    q = QuoteUpdateInputSerializer(data=request.data)
    q.is_valid(raise_exception=True)
    Quote.objects.filter(pk=pk).update(**q.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=QuotePartialUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: QuotePartialUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def quotes_partial_update(request: Request, pk: int) -> Response:
    q = QuotePartialUpdateInputSerializer(data=request.data)
    q.is_valid(raise_exception=True)
    Quote.objects.filter(pk=pk).update(**q.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineQuoteFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": QuoteFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(name="author", description="Filter by author", type=str),
    ],
)
@api_view(["GET"])
def quotes_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = QuoteFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data
    queryset = Quote.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("title")) is not None:
        queryset = queryset.filter(title=q)
    if (q := validated_data.get("author")) is not None:
        queryset = queryset.filter(author=q)
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    qs = QuoteFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(qs.data)


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
def quotes_delete(request: Request, pk: int) -> Response:
    Quote.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineProductListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ProductListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def products_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Product.objects.order_by("id").all(), request)
    ps = ProductListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: ProductDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def products_detail(request: Request, pk: int) -> Response:
    p = ProductDetailOutputSerializer(get_object_or_404(Product, pk=pk))
    return Response(p.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineProductSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ProductSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="q", description="Search query", type=str),
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def products_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Product.objects.order_by("id")
    else:
        queryset = Product.objects.filter(
            Q(id__icontains=q)
            | Q(title__icontains=q)
            | Q(brand__icontains=q)
            | Q(category__icontains=q)
            | Q(description__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = ProductSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    request=ProductCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: ProductCreateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def products_create(request: Request) -> Response:
    p = ProductCreateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Product.objects.create(**p.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=ProductUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: ProductUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def products_update(request: Request, pk: int) -> Response:
    p = ProductUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Product.objects.filter(pk=pk).update(**p.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=ProductPartialUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: ProductPartialUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def products_partial_update(request: Request, pk: int) -> Response:
    p = ProductPartialUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Product.objects.filter(pk=pk).update(**p.validated_data)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineProductFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ProductFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="title", description="Filter by title", type=str),
        OpenApiParameter(
            name="description", description="Filter by description", type=str
        ),
        OpenApiParameter(name="category", description="Filter by category", type=str),
        OpenApiParameter(name="price", description="Filter by price", type=float),
        OpenApiParameter(
            name="discount_percentage",
            description="Filter by discount_percentage",
            type=float,
        ),
        OpenApiParameter(name="rating", description="Filter by rating", type=float),
        OpenApiParameter(name="stock", description="Filter by stock", type=int),
        OpenApiParameter(name="tags", description="Filter by tags", type=str),
        OpenApiParameter(name="brand", description="Filter by brand", type=str),
        OpenApiParameter(name="sku", description="Filter by sku", type=str),
        OpenApiParameter(name="weight", description="Filter by weight", type=int),
        OpenApiParameter(name="width", description="Filter by width", type=float),
        OpenApiParameter(name="height", description="Filter by height", type=float),
        OpenApiParameter(name="depth", description="Filter by depth", type=float),
        OpenApiParameter(
            name="warranty_information",
            description="Filter by warranty_information",
            type=str,
        ),
        OpenApiParameter(
            name="shipping_information",
            description="Filter by shipping_information",
            type=str,
        ),
        OpenApiParameter(
            name="availability_status",
            description="Filter by availability_status",
            type=str,
        ),
        OpenApiParameter(
            name="return_policy", description="Filter by return_policy", type=str
        ),
        OpenApiParameter(
            name="minimum_order_quantity",
            description="Filter by minimum_order_quantity",
            type=int,
        ),
        OpenApiParameter(
            name="created_at", description="Filter by created_at", type=str
        ),
        OpenApiParameter(
            name="updated_at", description="Filter by updated_at", type=str
        ),
        OpenApiParameter(name="barcode", description="Filter by barcode", type=str),
        OpenApiParameter(name="qr_code", description="Filter by qr_code", type=str),
        OpenApiParameter(name="thumbnail", description="Filter by thumbnail", type=str),
    ],
)
@api_view(["GET"])
def products_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = ProductFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data
    queryset = Product.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("title")) is not None:
        queryset = queryset.filter(title=q)
    if (q := validated_data.get("category")) is not None:
        queryset = queryset.filter(category=q)
    if (q := validated_data.get("brand")) is not None:
        queryset = queryset.filter(brand=q)
    if (q := validated_data.get("price")) is not None:
        queryset = queryset.filter(price=q)
    if (q := validated_data.get("discount_percentage")) is not None:
        queryset = queryset.filter(discount_percentage=q)
    if (q := validated_data.get("rating")) is not None:
        queryset = queryset.filter(rating=q)
    if (q := validated_data.get("stock")) is not None:
        queryset = queryset.filter(stock=q)
    if (q := validated_data.get("tags")) is not None:
        queryset = queryset.filter(tags=q)
    if (q := validated_data.get("brand")) is not None:
        queryset = queryset.filter(brand=q)
    if (q := validated_data.get("sku")) is not None:
        queryset = queryset.filter(sku=q)
    if (q := validated_data.get("weight")) is not None:
        queryset = queryset.filter(weight=q)
    if (q := validated_data.get("width")) is not None:
        queryset = queryset.filter(width=q)
    if (q := validated_data.get("height")) is not None:
        queryset = queryset.filter(height=q)
    if (q := validated_data.get("depth")) is not None:
        queryset = queryset.filter(depth=q)
    if (q := validated_data.get("warranty_information")) is not None:
        queryset = queryset.filter(warranty_information=q)
    if (q := validated_data.get("shipping_information")) is not None:
        queryset = queryset.filter(shipping_information=q)
    if (q := validated_data.get("availability_status")) is not None:
        queryset = queryset.filter(availability_status=q)
    if (q := validated_data.get("return_policy")) is not None:
        queryset = queryset.filter(return_policy=q)
    if (q := validated_data.get("minimum_order_quantity")) is not None:
        queryset = queryset.filter(minimum_order_quantity=q)
    if (q := validated_data.get("barcode")) is not None:
        queryset = queryset.filter(barcode=q)
    if (q := validated_data.get("qr_code")) is not None:
        queryset = queryset.filter(qr_code=q)
    if (q := validated_data.get("thumbnail")) is not None:
        queryset = queryset.filter(thumbnail=q)
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = ProductFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


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
def products_delete(request: Request, pk: int) -> Response:
    Product.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineReviewListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ReviewListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def reviews_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Review.objects.order_by("id").all(), request)
    rs = ReviewListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: ReviewDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def reviews_detail(request: Request, pk: int) -> Response:
    r = ReviewDetailOutputSerializer(get_object_or_404(Review, pk=pk))
    return Response(r.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineReviewSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ReviewSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="q", description="Search query", type=str),
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def reviews_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Review.objects.order_by("id")
    else:
        queryset = Review.objects.filter(
            Q(id__icontains=q) | Q(comment__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    rs = ReviewSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@extend_schema(
    request=ReviewCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: ReviewCreateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def reviews_create(request: Request) -> Response:
    r = ReviewCreateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    body["product_id"] = body.pop("product")
    body["user_id"] = body.pop("user")
    Review.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=ReviewUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: ReviewUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def reviews_update(request: Request, pk: int) -> Response:
    r = ReviewUpdateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    body["product_id"] = body.pop("product")
    body["user_id"] = body.pop("user")
    Review.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=ReviewPartialUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: ReviewPartialUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def reviews_partial_update(request: Request, pk: int) -> Response:
    r = ReviewPartialUpdateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    if body.get("product") is not None:
        body["product_id"] = body.pop("product")
    if body.get("user") is not None:
        body["user_id"] = body.pop("user")
    Review.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineReviewFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": ReviewFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="rating", description="Filter by rating", type=int),
        OpenApiParameter(name="comment", description="Filter by comment", type=str),
        OpenApiParameter(name="date", description="Filter by date", type=str),
        OpenApiParameter(name="product", description="Filter by product", type=int),
        OpenApiParameter(name="user", description="Filter by user", type=int),
    ],
)
@api_view(["GET"])
def reviews_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = ReviewFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data
    queryset = Review.objects.order_by("id")
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("rating")) is not None:
        queryset = queryset.filter(rating=q)
    if (q := validated_data.get("product")) is not None:
        queryset = queryset.filter(product=q)
    if (q := validated_data.get("user")) is not None:
        queryset = queryset.filter(user=q)
    if (q := validated_data.get("comment")) is not None:
        queryset = queryset.filter(comment=q)
    if (q := validated_data.get("date")) is not None:
        queryset = queryset.filter(date=q)
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    rs = ReviewFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


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
def reviews_delete(request: Request, pk: int) -> Response:
    Review.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
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
        status.HTTP_200_OK: PostDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def posts_detail(request: Request, pk: int) -> Response:
    p = PostDetailOutputSerializer(get_object_or_404(Post, pk=pk))
    return Response(p.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
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
        OpenApiParameter(name="q", description="Search query", type=str),
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
            Q(id__icontains=q) | Q(title__icontains=q) | Q(body__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = PostSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@extend_schema(
    request=PostCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: PostCreateInputSerializer(),
    },
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
    responses={
        status.HTTP_200_OK: PostUpdateInputSerializer(),
    },
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
    responses={
        status.HTTP_200_OK: PostPartialUpdateInputSerializer(),
    },
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
        status.HTTP_200_OK: inline_serializer(
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
        OpenApiParameter(name="tags", description="Filter by tags", type=str),
        OpenApiParameter(name="likes", description="Filter by likes", type=int),
        OpenApiParameter(name="dislikes", description="Filter by dislikes", type=int),
        OpenApiParameter(name="views", description="Filter by views", type=int),
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
    if (q := validated_data.get("tags")) is not None:
        queryset = queryset.filter(tags=q)
    if (q := validated_data.get("likes")) is not None:
        queryset = queryset.filter(likes=q)
    if (q := validated_data.get("dislikes")) is not None:
        queryset = queryset.filter(dislikes=q)
    if (q := validated_data.get("views")) is not None:
        queryset = queryset.filter(views=q)
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    ps = PostFilterOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


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
def posts_delete(request: Request, pk: int) -> Response:
    Post.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


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
    page = paginator.paginate_queryset(Comment.objects.order_by("id").all(), request)
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
        OpenApiParameter(name="q", description="Search query", type=str),
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
            Q(id__icontains=q) | Q(body__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    cs = CommentSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    request=CommentCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: CommentCreateInputSerializer(),
    },
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
        status.HTTP_200_OK: CommentUpdateInputSerializer(),
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
        status.HTTP_200_OK: CommentPartialUpdateInputSerializer(),
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
        OpenApiParameter(name="body", description="Filter by body", type=str),
        OpenApiParameter(name="likes", description="Filter by likes", type=int),
        OpenApiParameter(name="post", description="Filter by post", type=int),
        OpenApiParameter(name="user", description="Filter by user", type=int),
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
    if (q := validated_data.get("body")) is not None:
        queryset = queryset.filter(body=q)
    if (q := validated_data.get("post")) is not None:
        queryset = queryset.filter(post=q)
    if (q := validated_data.get("user")) is not None:
        queryset = queryset.filter(user=q)
    if (q := validated_data.get("likes")) is not None:
        queryset = queryset.filter(likes=q)
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
        status.HTTP_200_OK: inline_serializer(
            "InlineCartListSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": CartListOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def carts_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(
        Cart.objects.select_related("user")
        .prefetch_related("products")
        .order_by("id")
        .all(),
        request,
    )
    carts_data = []
    for cart in page:
        carts_data.append(
            {
                "id": cart.id,
                "user": cart.user_id,
                "products": list(cart.products.values_list("id", flat=True)),
            }
        )
    cs = CartListOutputSerializer(carts_data, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: CartDetailOutputSerializer(),
    }
)
@api_view(["GET"])
def carts_detail(request: Request, pk: int) -> Response:
    cart = get_object_or_404(
        Cart.objects.select_related("user").prefetch_related("products"), pk=pk
    )
    cart_data = {
        "id": cart.id,
        "user": cart.user_id,
        "products": list(cart.products.values_list("id", flat=True)),
    }
    c = CartDetailOutputSerializer(cart_data)
    return Response(c.data)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineCartSearchSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": CartSearchOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="q", description="Search query", type=str),
        OpenApiParameter(name="page", description="Filter by page", type=int),
    ],
)
@api_view(["GET"])
def carts_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = Cart.objects.prefetch_related("products").order_by("id")
    else:
        queryset = (
            Cart.objects.prefetch_related("products")
            .filter(id__icontains=q)
            .filter(user__id__icontains=q)
            .order_by("id")
        )
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    carts_data = []
    for cart in page:
        carts_data.append(
            {
                "id": cart.id,
                "user": cart.user_id,
                "products": list(cart.products.values_list("id", flat=True)),
            }
        )
    cs = CartSearchOutputSerializer(carts_data, many=True)
    return paginator.get_paginated_response(cs.data)


@extend_schema(
    request=CartCreateInputSerializer,
    responses={
        status.HTTP_201_CREATED: CartCreateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["POST"])
@permission_classes([TokenPermission])
def carts_create(request: Request) -> Response:
    c = CartCreateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    user_id = body.pop("user")
    product_ids = body.pop("products")
    cart = Cart.objects.create(user_id=user_id)
    cart.products.set(product_ids)
    return Response(status=status.HTTP_201_CREATED)


@extend_schema(
    request=CartUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: CartUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PUT"])
@permission_classes([TokenPermission])
def carts_update(request: Request, pk: int) -> Response:
    c = CartUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    user_id = body.pop("user")
    product_ids = body.pop("products")
    Cart.objects.filter(pk=pk).update(user_id=user_id)
    cart = Cart.objects.get(pk=pk)
    cart.products.set(product_ids)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    request=CartPartialUpdateInputSerializer,
    responses={
        status.HTTP_200_OK: CartPartialUpdateInputSerializer(),
    },
    parameters=[
        OpenApiParameter(name="AUTH-TOKEN", location=OpenApiParameter.HEADER),
    ],
)
@api_view(["PATCH"])
@permission_classes([TokenPermission])
def carts_partial_update(request: Request, pk: int) -> Response:
    c = CartPartialUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    update_data = {}
    if body.get("user") is not None:
        update_data["user_id"] = body.pop("user")
    Cart.objects.filter(pk=pk).update(**update_data)
    if body.get("products") is not None:
        product_ids = body.pop("products")
        cart = Cart.objects.get(pk=pk)
        cart.products.set(product_ids)
    return Response(status=status.HTTP_200_OK)


@extend_schema(
    responses={
        status.HTTP_200_OK: inline_serializer(
            "InlineCartFilterSerializer",
            {
                "count": serializers.IntegerField(),
                "next": serializers.CharField(),
                "previous": serializers.CharField(),
                "results": CartFilterOutputSerializer(many=True),
            },
        )
    },
    parameters=[
        OpenApiParameter(name="page", description="Filter by page", type=int),
        OpenApiParameter(name="id", description="Filter by id", type=int),
        OpenApiParameter(name="user", description="Filter by user", type=int),
    ],
)
@api_view(["GET"])
def carts_filter(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    query_params = CartFilterInputSerializer(data=request.query_params)
    query_params.is_valid(raise_exception=True)
    validated_data = query_params.validated_data
    queryset = (
        Cart.objects.select_related("user").prefetch_related("products").order_by("id")
    )
    if (q := validated_data.get("id")) is not None:
        queryset = queryset.filter(id=q)
    if (q := validated_data.get("user")) is not None:
        queryset = queryset.filter(user=q)
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    carts_data = []
    for cart in page:
        carts_data.append(
            {
                "id": cart.id,
                "user": cart.user_id,
                "products": list(cart.products.values_list("id", flat=True)),
            }
        )
    cs = CartFilterOutputSerializer(carts_data, many=True)
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
def carts_delete(request: Request, pk: int) -> Response:
    Cart.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@extend_schema(responses={status.HTTP_200_OK: ProfileOutputSerializer()})
@api_view(["GET"])
def profile(request: Request, pk: int) -> Response:
    queryset = User.objects.prefetch_related(
        "todo_set",
        "recipe_set",
        "review_set",
        "cart_set__products",
        "post_set__comment_set",
    )
    user = get_object_or_404(queryset, id=pk)

    user_data = {
        "user_info": {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "maiden_name": user.maiden_name,
            "age": user.age,
            "gender": user.gender,
            "email": user.email,
            "phone": user.phone,
            "username": user.username,
            "password": user.password,
            "birthday": user.birthday,
            "image": user.image,
            "blood_group": user.blood_group,
            "height": user.height,
            "weight": user.weight,
            "eye_color": user.eye_color,
            "hair_color": user.hair_color,
            "hair_type": user.hair_type,
            "ip": user.ip,
            "address": user.address,
            "city": user.city,
            "state": user.state,
            "state_code": user.state_code,
            "postal_code": user.postal_code,
            "coordinates": user.coordinates,
            "country": user.country,
            "mac_address": user.mac_address,
            "university": user.university,
            "bank_card_expire": user.bank_card_expire,
            "bank_card_number": user.bank_card_number,
            "bank_card_type": user.bank_card_type,
            "bank_currency": user.bank_currency,
            "bank_iban": user.bank_iban,
            "company_department": user.company_department,
            "company_name": user.company_name,
            "company_title": user.company_title,
            "company_address": user.company_address,
            "company_city": user.company_city,
            "company_state": user.company_state,
            "company_state_code": user.company_state_code,
            "company_postal_code": user.company_postal_code,
            "company_coordinates": user.company_coordinates,
            "company_country": user.company_country,
            "ein": user.ein,
            "ssn": user.ssn,
            "user_agent": user.user_agent,
            "crypto_coint": user.crypto_coint,
            "crypto_wallet": user.crypto_wallet,
            "crypto_network": user.crypto_network,
            "role": user.role,
        },
        "todos": [
            {"title": todo.title, "completed": todo.completed}
            for todo in user.todo_set.all()
        ],
        "recipes": [
            {
                "name": recipe.name,
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions,
                "prep_time_minutes": recipe.prep_time_minutes,
                "cook_time_minutes": recipe.cook_time_minutes,
                "servings": recipe.servings,
                "difficulty": recipe.difficulty,
                "cuisine": recipe.cuisine,
                "calories_per_serving": recipe.calories_per_serving,
                "tags": recipe.tags,
                "image": recipe.image,
                "rating": recipe.rating,
                "review_count": recipe.review_count,
                "meal_type": recipe.meal_type,
            }
            for recipe in user.recipe_set.all()
        ],
        "reviews": [
            {
                "rating": review.rating,
                "comment": review.comment,
                "date": review.date,
            }
            for review in user.review_set.all()
        ],
        "carts": [
            {
                "products": [
                    {
                        "title": product.title,
                        "description": product.description,
                        "category": product.category,
                        "price": product.price,
                        "discount_percentage": product.discount_percentage,
                        "rating": product.rating,
                        "stock": product.stock,
                        "tags": product.tags,
                        "brand": product.brand,
                        "sku": product.sku,
                        "weight": product.weight,
                        "width": product.width,
                        "height": product.height,
                        "depth": product.depth,
                        "warranty_information": product.warranty_information,
                        "shipping_information": product.shipping_information,
                        "availability_status": product.availability_status,
                        "return_policy": product.return_policy,
                        "minimum_order_quantity": product.minimum_order_quantity,
                        "created_at": product.created_at,
                        "updated_at": product.updated_at,
                        "barcode": product.barcode,
                        "qr_code": product.qr_code,
                        "thumbnail": product.thumbnail,
                    }
                    for product in cart.products.all()
                ],
            }
            for cart in user.cart_set.all()
        ],
        "posts": [
            {
                "title": post.title,
                "body": post.body,
                "tags": post.tags,
                "likes": post.likes,
                "dislikes": post.dislikes,
                "views": post.views,
                "comments": [
                    {
                        "body": comment.body,
                        "likes": comment.likes,
                    }
                    for comment in post.comment_set.all()
                ],
            }
            for post in user.post_set.all()
        ],
    }
    serializer = ProfileOutputSerializer(user_data)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: UsersStatsOutputSerializer()},
)
@api_view(["GET"])
def users_stats(request: Request) -> Response:
    data = {
        "role_group": User.objects.values("role")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "company_state_group": User.objects.values("company_state")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "company_department_group": User.objects.values("company_department")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "bank_card_type_group": User.objects.values("bank_card_type")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "university_group": User.objects.values("university")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "state_group": User.objects.values("state")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "blood_group_group": User.objects.values("blood_group")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "gender_group": User.objects.values("gender")
        .annotate(count_users=Count("id"))
        .order_by("-count_users"),
        "other_group": User.objects.aggregate(
            min_age=Min("age"),
            max_age=Max("age"),
            avg_age=Avg("age"),
            min_height=Min("height"),
            max_height=Max("height"),
            avg_height=Avg("height"),
            min_weight=Min("weight"),
            max_weight=Max("weight"),
            avg_weight=Avg("weight"),
        ),
    }
    serializer = UsersStatsOutputSerializer(data)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: TodosStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def todos_stats(request: Request) -> Response:
    data = (
        Todo.objects.values("user_id")
        .annotate(
            count_todos=Count("id"),
            count_completed=Count("completed", filter=F("completed")),
            count_uncompleted=Count("completed", filter=~F("completed")),
        )
        .order_by("-count_completed")
    )
    serializer = TodosStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: RecipesStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def recipes_stats(request: Request) -> Response:
    data = (
        Recipe.objects.values("difficulty", "cuisine")
        .annotate(
            min_prep_time_minutes=Min("prep_time_minutes"),
            max_prep_time_minutes=Max("prep_time_minutes"),
            avg_prep_time_minutes=Avg("prep_time_minutes"),
            min_cook_time_minutes=Min("cook_time_minutes"),
            max_cook_time_minutes=Max("cook_time_minutes"),
            avg_cook_time_minutes=Avg("cook_time_minutes"),
            min_servings=Min("servings"),
            max_servings=Max("servings"),
            avg_servings=Avg("servings"),
            min_calories_per_serving=Min("calories_per_serving"),
            max_calories_per_serving=Max("calories_per_serving"),
            avg_calories_per_serving=Avg("calories_per_serving"),
            min_rating=Min("rating"),
            max_rating=Max("rating"),
            avg_rating=Avg("rating"),
            sum_review_count=Sum("review_count"),
        )
        .order_by("-sum_review_count", "-avg_rating")
    )
    serializer = RecipesStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: QuotesStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def quotes_stats(request: Request) -> Response:
    data = (
        Quote.objects.values("author")
        .annotate(count_quotes=Count("id"))
        .order_by("-count_quotes")
    )
    serializer = QuotesStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: ProductsStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def products_stats(request: Request) -> Response:
    data = (
        Product.objects.values("category")
        .annotate(
            count_products=Count("id"),
            avg_price=Avg("price"),
            max_price=Max("price"),
            min_price=Min("price"),
            avg_discount_percentage=Avg("discount_percentage"),
            max_discount_percentage=Max("discount_percentage"),
            min_discount_percentage=Min("discount_percentage"),
            avg_rating=Avg("rating"),
            max_rating=Max("rating"),
            min_rating=Min("rating"),
            sum_stock=Sum("stock"),
        )
        .order_by("-count_products")
    )
    serializer = ProductsStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: ReviewsStatsOutputSerializer()},
)
@api_view(["GET"])
def reviews_stats(request: Request) -> Response:
    data = Review.objects.aggregate(
        count_reviews=Count("id"),
        avg_rating=Avg("rating"),
        count_unique_products=Count("product", distinct=True),
        count_unique_users=Count("user", distinct=True),
        max_rating=Max("rating"),
        min_rating=Min("rating"),
    )
    serializer = ReviewsStatsOutputSerializer(data)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: PostsStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def posts_stats(request: Request) -> Response:
    data = (
        Post.objects.values("user_id")
        .annotate(
            count_posts=Count("id"),
            sum_views=Sum("views"),
            sum_likes=Sum("likes"),
            sum_dislikes=Sum("dislikes"),
        )
        .order_by("-sum_views")
    )
    serializer = PostsStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: CommentsStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def comments_stats(request: Request) -> Response:
    data = (
        Comment.objects.values("post_id")
        .annotate(
            sum_likes=Sum("likes"),
            count_comments=Count("id"),
            avg_likes=Avg("likes"),
            max_likes=Max("likes"),
            min_likes=Min("likes"),
        )
        .order_by("-sum_likes")
    )
    serializer = CommentsStatsOutputSerializer(data, many=True)
    return Response(serializer.data)


@extend_schema(
    responses={status.HTTP_200_OK: CartStatsOutputSerializer(many=True)},
)
@api_view(["GET"])
def carts_stats(request: Request) -> Response:
    data = Cart.objects.annotate(total_check=Sum("products__price")).values(
        "id", "user_id", "total_check"
    )
    serializer = CartStatsOutputSerializer(data, many=True)
    return Response(serializer.data)
