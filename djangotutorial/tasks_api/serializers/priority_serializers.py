from rest_framework import serializers


class TasksPriorityListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    active = serializers.BooleanField()


class TasksPriorityDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    active = serializers.BooleanField()


class TasksPrioritySearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    active = serializers.BooleanField()


class TasksPriorityCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    active = serializers.BooleanField(default=True)


class TasksPriorityUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    active = serializers.BooleanField()


class TasksPriorityPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    active = serializers.BooleanField(required=False)


class TasksPriorityFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    active = serializers.BooleanField()


class TasksPriorityFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    active = serializers.BooleanField(required=False, allow_null=True)


class TasksPriorityStatsOutputSerializer(serializers.Serializer):
    count_priorities = serializers.IntegerField()
