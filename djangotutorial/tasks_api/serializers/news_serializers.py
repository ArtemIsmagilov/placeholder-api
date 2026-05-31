from rest_framework import serializers


class TasksNewsListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.CharField()
    description = serializers.CharField()
    project = serializers.IntegerField(source="project_id")
    author = serializers.IntegerField(source="author_id")
    created_on = serializers.DateTimeField()


class TasksNewsDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.CharField()
    description = serializers.CharField()
    project = serializers.IntegerField(source="project_id")
    author = serializers.IntegerField(source="author_id")
    created_on = serializers.DateTimeField()


class TasksNewsSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.CharField()
    description = serializers.CharField()
    project = serializers.IntegerField(source="project_id")
    author = serializers.IntegerField(source="author_id")
    created_on = serializers.DateTimeField()


class TasksNewsCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    summary = serializers.CharField()
    description = serializers.CharField()
    project = serializers.IntegerField()
    author = serializers.IntegerField()


class TasksNewsUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    summary = serializers.CharField()
    description = serializers.CharField()
    project = serializers.IntegerField()
    author = serializers.IntegerField()


class TasksNewsPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    summary = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    project = serializers.IntegerField(required=False)
    author = serializers.IntegerField(required=False)


class TasksNewsFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.CharField()
    description = serializers.CharField()
    project = serializers.IntegerField(source="project_id")
    author = serializers.IntegerField(source="author_id")
    created_on = serializers.DateTimeField()


class TasksNewsFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    project = serializers.IntegerField(required=False)
    author = serializers.IntegerField(required=False)


class TasksNewsStatsOutputSerializer(serializers.Serializer):
    project = serializers.IntegerField(source="project_id")
    count_news = serializers.IntegerField()
