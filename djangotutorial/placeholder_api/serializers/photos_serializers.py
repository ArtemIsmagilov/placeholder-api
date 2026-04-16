from rest_framework import serializers


class PhotoListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField(source="album_id")


class PhotoDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField(source="album_id")


class PhotoSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField(source="album_id")


class PhotoCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField()


class PhotoUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField()


class PhotoPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    url = serializers.URLField(required=False)
    thumbnail_url = serializers.URLField(required=False)
    album = serializers.IntegerField(required=False)
