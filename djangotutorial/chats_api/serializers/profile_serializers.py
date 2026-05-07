from rest_framework import serializers


class ChatsUserProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsProfileUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()


class ChatsProfileAuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()


class ChatsProfileMessageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField()
    author = ChatsProfileAuthorSerializer()


class ChatsProfileChatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    created_at = serializers.DateTimeField()
    users = ChatsProfileUserSerializer(many=True)
    messages = ChatsProfileMessageSerializer(many=True)


class ChatsProfileOutputSerializer(serializers.Serializer):
    user_info = ChatsUserProfileSerializer()
    chats = ChatsProfileChatSerializer(many=True)
