from rest_framework import serializers


class CommentListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class CommentDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class CommentSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class CommentCreateInputSerializer(serializers.Serializer):
    body = serializers.CharField()
    likes = serializers.IntegerField(required=False, default=0)
    post = serializers.IntegerField()


class CommentUpdateInputSerializer(serializers.Serializer):
    body = serializers.CharField()
    likes = serializers.IntegerField(required=False)
    post = serializers.IntegerField()


class CommentPartialUpdateInputSerializer(serializers.Serializer):
    body = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    post = serializers.IntegerField(required=False)


class CommentFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    likes = serializers.IntegerField()
    post = serializers.IntegerField(source="post_id")


class CommentFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    body = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    post = serializers.IntegerField(required=False)
