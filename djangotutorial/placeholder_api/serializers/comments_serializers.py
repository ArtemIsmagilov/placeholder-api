from rest_framework import serializers


class PlaceholderCommentListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField(source="post_id")


class PlaceholderCommentDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField(source="post_id")


class PlaceholderCommentSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField(source="post_id")


class PlaceholderCommentCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField()


class PlaceholderCommentUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField()


class PlaceholderCommentPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    body = serializers.CharField(required=False)
    post = serializers.IntegerField(required=False)


class PlaceholderCommentFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField(source="post_id")


class PlaceholderCommentFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    body = serializers.CharField(required=False)
    post = serializers.IntegerField(required=False)


class PlaceholderCommentStatsOutputSerializer(serializers.Serializer):
    post = serializers.IntegerField(source="post_id")
    count_comments = serializers.IntegerField()
