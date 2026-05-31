from rest_framework import serializers


class TasksCommentListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()
    author = serializers.IntegerField(source="author_id")
    some_news = serializers.IntegerField(source="some_news_id")
    created_on = serializers.DateTimeField()


class TasksCommentDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()
    author = serializers.IntegerField(source="author_id")
    some_news = serializers.IntegerField(source="some_news_id")
    created_on = serializers.DateTimeField()


class TasksCommentSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()
    author = serializers.IntegerField(source="author_id")
    some_news = serializers.IntegerField(source="some_news_id")
    created_on = serializers.DateTimeField()


class TasksCommentCreateInputSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.IntegerField()
    some_news = serializers.IntegerField()


class TasksCommentUpdateInputSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.IntegerField()
    some_news = serializers.IntegerField()


class TasksCommentPartialUpdateInputSerializer(serializers.Serializer):
    content = serializers.CharField(required=False)
    author = serializers.IntegerField(required=False)
    some_news = serializers.IntegerField(required=False)


class TasksCommentFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()
    author = serializers.IntegerField(source="author_id")
    some_news = serializers.IntegerField(source="some_news_id")
    created_on = serializers.DateTimeField()


class TasksCommentFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    author = serializers.IntegerField(required=False)
    some_news = serializers.IntegerField(required=False)


class TasksCommentStatsOutputSerializer(serializers.Serializer):
    some_news = serializers.IntegerField(source="some_news_id")
    count_comments = serializers.IntegerField()
