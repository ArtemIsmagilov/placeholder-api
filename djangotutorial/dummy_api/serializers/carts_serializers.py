from rest_framework import serializers


class CartListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return [p.id for p in obj.products.all()]


class CartDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return [p.id for p in obj.products.all()]


class CartSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return [p.id for p in obj.products.all()]


class CartCreateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartUpdateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartPartialUpdateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
    products = serializers.ListField(child=serializers.IntegerField())


class CartFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return [p.id for p in obj.products.all()]


class CartFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class CartStatsOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    total_check = serializers.FloatField()
