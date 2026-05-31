from rest_framework import serializers


class TasksCategoryListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksCategoryDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksCategorySearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksCategoryCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()


class TasksCategoryUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()


class TasksCategoryPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)


class TasksCategoryFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksCategoryFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


class TasksCategoryStatsOutputSerializer(serializers.Serializer):
    count_categories = serializers.IntegerField()
