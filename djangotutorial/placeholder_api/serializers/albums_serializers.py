from rest_framework import serializers


class AlbumListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class AlbumDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class AlbumSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class AlbumCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    user = serializers.IntegerField()


class AlbumUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    user = serializers.IntegerField()


class AlbumPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class AlbumFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class AlbumFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class AlbumStatsOutputSerializer(serializers.Serializer):
    user = serializers.IntegerField(source="user_id")
    count_albums = serializers.IntegerField()
