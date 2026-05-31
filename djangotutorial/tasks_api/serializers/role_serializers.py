from rest_framework import serializers


class TasksRoleListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksRoleDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksRoleSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksRoleCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()


class TasksRoleUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()


class TasksRolePartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)


class TasksRoleFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksRoleFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


class TasksRoleStatsOutputSerializer(serializers.Serializer):
    count_roles = serializers.IntegerField()
