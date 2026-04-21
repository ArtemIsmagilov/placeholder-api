from django.shortcuts import get_object_or_404
from django.db.models import Q
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
)
from dummy_api.permissions import TokenPermission


@api_view(["GET"])
def users_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(User.objects.order_by("id").all(), request)
    us = UserListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@api_view(["GET"])
def users_detail(request: Request, pk: int) -> Response:
    u = UserDetailOutputSerializer(get_object_or_404(User, pk=pk))
    return Response(u.data)


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
            | Q(username__icontains=q)
            | Q(email__icontains=q)
        ).order_by("id")
    paginator = Pagination()
    page = paginator.paginate_queryset(queryset, request)
    us = UserSearchOutputSerializer(page, many=True)
    return paginator.get_paginated_response(us.data)


@api_view(["POST"])
@permission_classes([TokenPermission])
def users_create(request: Request) -> Response:
    u = UserCreateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.create(**u.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([TokenPermission])
def users_update(request: Request, pk: int) -> Response:
    u = UserUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
@permission_classes([TokenPermission])
def users_partial_update(request: Request, pk: int) -> Response:
    u = UserPartialUpdateInputSerializer(data=request.data)
    u.is_valid(raise_exception=True)
    User.objects.filter(pk=pk).update(**u.validated_data)
    return Response(status=status.HTTP_200_OK)


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
    if (q := validated_data.get("snn")) is not None:
        queryset = queryset.filter(snn=q)
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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def users_delete(request: Request, pk: int) -> Response:
    User.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def todos_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Todo.objects.order_by("id").all(), request)
    ts = TodoListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ts.data)


@api_view(["GET"])
def todos_detail(request: Request, pk: int) -> Response:
    t = TodoDetailOutputSerializer(get_object_or_404(Todo, pk=pk))
    return Response(t.data)


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


@api_view(["POST"])
@permission_classes([TokenPermission])
def todos_create(request: Request) -> Response:
    t = TodoCreateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    body["user_id"] = body.pop("user")
    Todo.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([TokenPermission])
def todos_update(request: Request, pk: int) -> Response:
    t = TodoUpdateInputSerializer(data=request.data)
    t.is_valid(raise_exception=True)
    body = t.validated_data
    body["user_id"] = body.pop("user")
    Todo.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def todos_delete(request: Request, pk: int) -> Response:
    Todo.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def recipes_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Recipe.objects.order_by("id").all(), request)
    rs = RecipeListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@api_view(["GET"])
def recipes_detail(request: Request, pk: int) -> Response:
    r = RecipeDetailOutputSerializer(get_object_or_404(Recipe, pk=pk))
    return Response(r.data)


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


@api_view(["POST"])
@permission_classes([TokenPermission])
def recipes_create(request: Request) -> Response:
    r = RecipeCreateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    body["user_id"] = body.pop("user")
    Recipe.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([TokenPermission])
def recipes_update(request: Request, pk: int) -> Response:
    r = RecipeUpdateInputSerializer(data=request.data)
    r.is_valid(raise_exception=True)
    body = r.validated_data
    body["user_id"] = body.pop("user")
    Recipe.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def recipes_delete(request: Request, pk: int) -> Response:
    Recipe.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def quotes_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Quote.objects.order_by("id").all(), request)
    qs = QuoteListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(qs.data)


@api_view(["GET"])
def quotes_detail(request: Request, pk: int) -> Response:
    q = QuoteDetailOutputSerializer(get_object_or_404(Quote, pk=pk))
    return Response(q.data)


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


@api_view(["POST"])
@permission_classes([TokenPermission])
def quotes_create(request: Request) -> Response:
    q = QuoteCreateInputSerializer(data=request.data)
    q.is_valid(raise_exception=True)
    Quote.objects.create(**q.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([TokenPermission])
def quotes_update(request: Request, pk: int) -> Response:
    q = QuoteUpdateInputSerializer(data=request.data)
    q.is_valid(raise_exception=True)
    Quote.objects.filter(pk=pk).update(**q.validated_data)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
@permission_classes([TokenPermission])
def quotes_partial_update(request: Request, pk: int) -> Response:
    q = QuotePartialUpdateInputSerializer(data=request.data)
    q.is_valid(raise_exception=True)
    Quote.objects.filter(pk=pk).update(**q.validated_data)
    return Response(status=status.HTTP_200_OK)


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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def quotes_delete(request: Request, pk: int) -> Response:
    Quote.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def products_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Product.objects.order_by("id").all(), request)
    ps = ProductListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@api_view(["GET"])
def products_detail(request: Request, pk: int) -> Response:
    p = ProductDetailOutputSerializer(get_object_or_404(Product, pk=pk))
    return Response(p.data)


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


@api_view(["POST"])
@permission_classes([TokenPermission])
def products_create(request: Request) -> Response:
    p = ProductCreateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Product.objects.create(**p.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([TokenPermission])
def products_update(request: Request, pk: int) -> Response:
    p = ProductUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Product.objects.filter(pk=pk).update(**p.validated_data)
    return Response(status=status.HTTP_200_OK)


@api_view(["PATCH"])
@permission_classes([TokenPermission])
def products_partial_update(request: Request, pk: int) -> Response:
    p = ProductPartialUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    Product.objects.filter(pk=pk).update(**p.validated_data)
    return Response(status=status.HTTP_200_OK)


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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def products_delete(request: Request, pk: int) -> Response:
    Product.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def reviews_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Review.objects.order_by("id").all(), request)
    rs = ReviewListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(rs.data)


@api_view(["GET"])
def reviews_detail(request: Request, pk: int) -> Response:
    r = ReviewDetailOutputSerializer(get_object_or_404(Review, pk=pk))
    return Response(r.data)


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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def reviews_delete(request: Request, pk: int) -> Response:
    Review.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def posts_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Post.objects.order_by("id").all(), request)
    ps = PostListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(ps.data)


@api_view(["GET"])
def posts_detail(request: Request, pk: int) -> Response:
    p = PostDetailOutputSerializer(get_object_or_404(Post, pk=pk))
    return Response(p.data)


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


@api_view(["POST"])
@permission_classes([TokenPermission])
def posts_create(request: Request) -> Response:
    p = PostCreateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["user_id"] = body.pop("user")
    Post.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([TokenPermission])
def posts_update(request: Request, pk: int) -> Response:
    p = PostUpdateInputSerializer(data=request.data)
    p.is_valid(raise_exception=True)
    body = p.validated_data
    body["user_id"] = body.pop("user")
    Post.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def posts_delete(request: Request, pk: int) -> Response:
    Post.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def comments_list(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    paginator = Pagination()
    page = paginator.paginate_queryset(Comment.objects.order_by("id").all(), request)
    cs = CommentListOutputSerializer(page, many=True)
    return paginator.get_paginated_response(cs.data)


@api_view(["GET"])
def comments_detail(request: Request, pk: int) -> Response:
    c = CommentDetailOutputSerializer(get_object_or_404(Comment, pk=pk))
    return Response(c.data)


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


@api_view(["POST"])
@permission_classes([TokenPermission])
def comments_create(request: Request) -> Response:
    c = CommentCreateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["post_id"] = body.pop("post")
    Comment.objects.create(**body)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([TokenPermission])
def comments_update(request: Request, pk: int) -> Response:
    c = CommentUpdateInputSerializer(data=request.data)
    c.is_valid(raise_exception=True)
    body = c.validated_data
    body["post_id"] = body.pop("post")
    Comment.objects.filter(pk=pk).update(**body)
    return Response(status=status.HTTP_200_OK)


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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def comments_delete(request: Request, pk: int) -> Response:
    Comment.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)


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


@api_view(["GET"])
def carts_search(request: Request) -> Response:
    class Pagination(PageNumberPagination):
        page_size = 10

    if (q := request.query_params.get("q")) is None:
        queryset = (
            Cart.objects.select_related("user")
            .prefetch_related("products")
            .order_by("id")
        )
    else:
        queryset = (
            Cart.objects.select_related("user")
            .prefetch_related("products")
            .filter(id__icontains=q)
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


@api_view(["DELETE"])
@permission_classes([TokenPermission])
def carts_delete(request: Request, pk: int) -> Response:
    Cart.objects.filter(pk=pk).delete()
    return Response(status=status.HTTP_200_OK)
