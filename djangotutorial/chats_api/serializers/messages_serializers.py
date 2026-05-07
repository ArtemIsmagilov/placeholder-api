from rest_framework import serializers


class ChatsMessageListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    chat = serializers.IntegerField(source="chat_id")
    author = serializers.IntegerField(source="author_id")
    text = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsMessageDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    chat = serializers.IntegerField(source="chat_id")
    author = serializers.IntegerField(source="author_id")
    text = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsMessageSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    chat = serializers.IntegerField(source="chat_id")
    author = serializers.IntegerField(source="author_id")
    text = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsMessageCreateInputSerializer(serializers.Serializer):
    chat = serializers.IntegerField()
    author = serializers.IntegerField()
    text = serializers.CharField()


class ChatsMessageUpdateInputSerializer(serializers.Serializer):
    chat = serializers.IntegerField()
    author = serializers.IntegerField()
    text = serializers.CharField()


class ChatsMessagePartialUpdateInputSerializer(serializers.Serializer):
    chat = serializers.IntegerField(required=False)
    author = serializers.IntegerField(required=False)
    text = serializers.CharField(required=False)


class ChatsMessageFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    chat = serializers.IntegerField(source="chat_id")
    author = serializers.IntegerField(source="author_id")
    text = serializers.CharField()
    created_at = serializers.DateTimeField()


class ChatsMessageFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    chat = serializers.IntegerField(required=False)
    author = serializers.IntegerField(required=False)


class ChatsMessageStatsOutputSerializer(serializers.Serializer):
    chat = serializers.IntegerField(source="chat_id")
    count_messages = serializers.IntegerField()
