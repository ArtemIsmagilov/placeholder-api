from rest_framework import serializers


class PlaceholderPhotoListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField(source="album_id")


class PlaceholderPhotoDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField(source="album_id")


class PlaceholderPhotoSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField(source="album_id")


class PlaceholderPhotoCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField()


class PlaceholderPhotoUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField()


class PlaceholderPhotoPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    url = serializers.URLField(required=False)
    thumbnail_url = serializers.URLField(required=False)
    album = serializers.IntegerField(required=False)


class PlaceholderPhotoFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    album = serializers.IntegerField(source="album_id")


class PlaceholderPhotoFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    url = serializers.URLField(required=False)
    thumbnail_url = serializers.URLField(required=False)
    album = serializers.IntegerField(required=False)


class PlaceholderPhotoStatsOutputSerializer(serializers.Serializer):
    album = serializers.IntegerField(source="album_id")
    count_photos = serializers.IntegerField()
