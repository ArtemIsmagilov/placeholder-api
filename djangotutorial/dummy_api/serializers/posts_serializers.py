from rest_framework import serializers


class DummyPostListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class DummyPostDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class DummyPostSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class DummyPostCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField()


class DummyPostUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField()


class DummyPostPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    tags = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    dislikes = serializers.IntegerField(required=False)
    views = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class DummyPostFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class DummyPostFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    tags = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    dislikes = serializers.IntegerField(required=False)
    views = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class DummyPostStatsOutputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    count_posts = serializers.IntegerField()
    sum_views = serializers.IntegerField()
    sum_likes = serializers.IntegerField()
    sum_dislikes = serializers.IntegerField()
