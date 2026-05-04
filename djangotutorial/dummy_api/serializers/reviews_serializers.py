from rest_framework import serializers


class DummyReviewListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class DummyReviewDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class DummyReviewSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class DummyReviewCreateInputSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField()
    user = serializers.IntegerField()


class DummyReviewUpdateInputSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField()
    user = serializers.IntegerField()


class DummyReviewPartialUpdateInputSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=False)
    comment = serializers.CharField(required=False)
    date = serializers.DateTimeField(required=False)
    product = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class DummyReviewFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class DummyReviewFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    rating = serializers.IntegerField(required=False)
    comment = serializers.CharField(required=False)
    date = serializers.DateTimeField(required=False)
    product = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class DummyReviewStatsOutputSerializer(serializers.Serializer):
    count_reviews = serializers.IntegerField()
    avg_rating = serializers.FloatField()
    count_unique_products = serializers.IntegerField()
    count_unique_users = serializers.IntegerField()
    max_rating = serializers.IntegerField()
    min_rating = serializers.IntegerField()
