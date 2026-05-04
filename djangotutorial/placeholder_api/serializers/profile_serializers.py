from rest_framework import serializers


class PlaceholderUserProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.URLField()
    company = serializers.CharField()


class PlaceholderTodoProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()


class PlaceholderPhotoProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()


class PlaceholderAlbumProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    pictures = PlaceholderPhotoProfileSerializer(many=True)


class PlaceholderCommentProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()


class PlaceholderPostProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    comments = PlaceholderCommentProfileSerializer(many=True)


class PlaceholderProfileOutputSerializer(serializers.Serializer):
    user_info = PlaceholderUserProfileSerializer()
    todos = PlaceholderTodoProfileSerializer(many=True)
    albums = PlaceholderAlbumProfileSerializer(many=True)
    posts = PlaceholderPostProfileSerializer(many=True)
