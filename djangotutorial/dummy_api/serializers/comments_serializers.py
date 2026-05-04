from rest_framework import serializers


class DummyCommentListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class DummyCommentDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class DummyCommentSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class DummyCommentCreateInputSerializer(serializers.Serializer):
    body = serializers.CharField()
    likes = serializers.IntegerField(required=False, default=0)
    post = serializers.IntegerField()


class DummyCommentUpdateInputSerializer(serializers.Serializer):
    body = serializers.CharField()
    likes = serializers.IntegerField(required=False)
    post = serializers.IntegerField()


class DummyCommentPartialUpdateInputSerializer(serializers.Serializer):
    body = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    post = serializers.IntegerField(required=False)


class DummyCommentFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class DummyCommentFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    body = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    post = serializers.IntegerField(required=False)


class DummyCommentStatsOutputSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    sum_likes = serializers.IntegerField()
    count_comments = serializers.IntegerField()
    avg_likes = serializers.FloatField()
    max_likes = serializers.IntegerField()
    min_likes = serializers.IntegerField()
