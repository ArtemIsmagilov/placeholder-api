from rest_framework import serializers


class UserListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class UserDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class UserSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class UserCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class UserUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class UserPartialUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    company = serializers.CharField(required=False)


class UserFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    website = serializers.CharField()
    company = serializers.CharField()


class UserFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    company = serializers.CharField(required=False)


class UserStatsOutputSerializer(serializers.Serializer):
    company = serializers.CharField()
    count_users = serializers.IntegerField()
