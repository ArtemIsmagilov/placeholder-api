from rest_framework import serializers


class PlaceholderAlbumListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderAlbumDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderAlbumSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderAlbumCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    user = serializers.IntegerField()


class PlaceholderAlbumUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    user = serializers.IntegerField()


class PlaceholderAlbumPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class PlaceholderAlbumFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderAlbumFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class PlaceholderAlbumStatsOutputSerializer(serializers.Serializer):
    user = serializers.IntegerField(source="user_id")
    count_albums = serializers.IntegerField()
