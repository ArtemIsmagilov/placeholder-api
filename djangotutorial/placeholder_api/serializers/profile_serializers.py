from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.URLField()
    company = serializers.CharField()


class TodoProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()


class PhotoProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()


class AlbumProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    pictures = PhotoProfileSerializer(many=True)


class CommentProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()


class PostProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    comments = CommentProfileSerializer(many=True)


class ProfileOutputSerializer(serializers.Serializer):
    user_info = UserProfileSerializer()
    todos = TodoProfileSerializer(many=True)
    albums = AlbumProfileSerializer(many=True)
    posts = PostProfileSerializer(many=True)
