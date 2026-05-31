from rest_framework import serializers


class TasksGroupListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksGroupDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksGroupSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksGroupCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()


class TasksGroupUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()


class TasksGroupPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)


class TasksGroupFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TasksGroupFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


class TasksGroupStatsOutputSerializer(serializers.Serializer):
    count_groups = serializers.IntegerField()
