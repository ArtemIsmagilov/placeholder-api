from rest_framework import serializers


class ReviewListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class ReviewDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class ReviewSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class ReviewCreateInputSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField()
    user = serializers.IntegerField()


class ReviewUpdateInputSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField()
    user = serializers.IntegerField()


class ReviewPartialUpdateInputSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=False)
    comment = serializers.CharField(required=False)
    date = serializers.DateTimeField(required=False)
    product = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class ReviewFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()
    product = serializers.IntegerField(source="product_id")
    user = serializers.IntegerField(source="user_id")


class ReviewFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    rating = serializers.IntegerField(required=False)
    comment = serializers.CharField(required=False)
    date = serializers.DateTimeField(required=False)
    product = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class ReviewStatsOutputSerializer(serializers.Serializer):
    count_reviews = serializers.IntegerField()
    avg_rating = serializers.FloatField()
    count_unique_products = serializers.IntegerField()
    count_unique_users = serializers.IntegerField()
    max_rating = serializers.IntegerField()
    min_rating = serializers.IntegerField()
