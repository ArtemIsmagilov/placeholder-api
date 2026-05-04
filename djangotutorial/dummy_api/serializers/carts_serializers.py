from rest_framework import serializers


class DummyCartListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj) -> list[int]:
        return [p.id for p in obj.products.all()]


class DummyCartDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj) -> list[int]:
        return [p.id for p in obj.products.all()]


class DummyCartSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj) -> list[int]:
        return [p.id for p in obj.products.all()]


class DummyCartCreateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class DummyCartUpdateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class DummyCartPartialUpdateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
    products = serializers.ListField(child=serializers.IntegerField())


class DummyCartFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    products = serializers.SerializerMethodField()

    def get_products(self, obj) -> list[int]:
        return [p.id for p in obj.products.all()]


class DummyCartFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class DummyCartStatsOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")
    total_check = serializers.FloatField()
