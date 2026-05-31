from rest_framework import serializers


class TasksStatusListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    is_close = serializers.BooleanField()
    description = serializers.CharField(allow_null=True)


class TasksStatusDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    is_close = serializers.BooleanField()
    description = serializers.CharField(allow_null=True)


class TasksStatusSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    is_close = serializers.BooleanField()
    description = serializers.CharField(allow_null=True)


class TasksStatusCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_close = serializers.BooleanField(default=False)
    description = serializers.CharField(required=False, allow_null=True)


class TasksStatusUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_close = serializers.BooleanField()
    description = serializers.CharField(required=False, allow_null=True)


class TasksStatusPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    is_close = serializers.BooleanField(required=False)
    description = serializers.CharField(required=False, allow_null=True)


class TasksStatusFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    is_close = serializers.BooleanField()
    description = serializers.CharField(allow_null=True)


class TasksStatusFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    is_close = serializers.BooleanField(required=False, allow_null=True)


class TasksStatusStatsOutputSerializer(serializers.Serializer):
    count_statuses = serializers.IntegerField()
