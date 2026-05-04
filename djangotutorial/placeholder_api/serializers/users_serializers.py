from rest_framework import serializers


class PlaceholderUserListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class PlaceholderUserDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class PlaceholderUserSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class PlaceholderUserCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class PlaceholderUserUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class PlaceholderUserPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    company = serializers.CharField(required=False)


class PlaceholderUserFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class PlaceholderUserFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    company = serializers.CharField(required=False)


class PlaceholderUserStatsOutputSerializer(serializers.Serializer):
    company = serializers.CharField()
    count_users = serializers.IntegerField()
