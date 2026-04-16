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
