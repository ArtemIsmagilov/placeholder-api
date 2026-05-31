from rest_framework import serializers


class TasksProjectListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    identifier = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_public = serializers.BooleanField()
    parent = serializers.IntegerField(source="parent_id", allow_null=True)
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksProjectDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    identifier = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_public = serializers.BooleanField()
    parent = serializers.IntegerField(source="parent_id", allow_null=True)
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksProjectSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    identifier = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_public = serializers.BooleanField()
    parent = serializers.IntegerField(source="parent_id", allow_null=True)
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksProjectCreateInputSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_public = serializers.BooleanField(default=True)
    parent = serializers.IntegerField(required=False, allow_null=True)


class TasksProjectUpdateInputSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_public = serializers.BooleanField()
    parent = serializers.IntegerField(required=False, allow_null=True)


class TasksProjectPartialUpdateInputSerializer(serializers.Serializer):
    identifier = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    is_public = serializers.BooleanField(required=False)
    parent = serializers.IntegerField(required=False, allow_null=True)


class TasksProjectFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    identifier = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_public = serializers.BooleanField()
    parent = serializers.IntegerField(source="parent_id", allow_null=True)
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksProjectFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    identifier = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    is_public = serializers.BooleanField(required=False, allow_null=True)


class TasksProjectStatsOutputSerializer(serializers.Serializer):
    count_projects = serializers.IntegerField()
