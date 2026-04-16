from rest_framework import serializers


class CommentiListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField(source="post_id")


class CommentDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField(source="post_id")


class CommentSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField(source="post_id")


class CommentCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField()


class CommentUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    post = serializers.IntegerField()


class CommentPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    body = serializers.CharField(required=False)
    post = serializers.IntegerField(required=False)
