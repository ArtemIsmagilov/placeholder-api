from rest_framework import serializers


class CartListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartCreateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartUpdateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartPartialUpdateInputSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
    products = serializers.ListField(child=serializers.IntegerField(), required=False)


class CartFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField()
    products = serializers.ListField(child=serializers.IntegerField())


class CartFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)
