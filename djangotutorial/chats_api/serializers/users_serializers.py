from rest_framework import serializers


class ChatsUserListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsUserDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsUserSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsUserCreateInputSerializer(serializers.Serializer):
    username = serializers.CharField()


class ChatsUserUpdateInputSerializer(serializers.Serializer):
    username = serializers.CharField()


class ChatsUserPartialUpdateInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)


class ChatsUserFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsUserFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False)


class ChatsUserStatsOutputSerializer(serializers.Serializer):
    count_users = serializers.IntegerField()
