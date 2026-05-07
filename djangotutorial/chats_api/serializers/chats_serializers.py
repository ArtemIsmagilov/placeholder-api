from rest_framework import serializers


class ChatsChatListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    users = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()

    def get_users(self, obj):
        return [u.id for u in obj.users.all()]


class ChatsChatDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    users = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()

    def get_users(self, obj):
        return [u.id for u in obj.users.all()]


class ChatsChatSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    users = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()

    def get_users(self, obj):
        return [u.id for u in obj.users.all()]


class ChatsChatCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    users = serializers.ListField(child=serializers.IntegerField(), required=False)


class ChatsChatUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    users = serializers.ListField(child=serializers.IntegerField(), required=False)


class ChatsChatPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    users = serializers.ListField(child=serializers.IntegerField(), required=False)


class ChatsChatFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    users = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()

    def get_users(self, obj):
        return [u.id for u in obj.users.all()]


class ChatsChatFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


class ChatsChatStatsOutputSerializer(serializers.Serializer):
    count_chats = serializers.IntegerField()
