from rest_framework import serializers


class TasksUserListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    login = serializers.CharField()
    admin = serializers.BooleanField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.EmailField()
    role = serializers.IntegerField(source="role_id")
    group = serializers.IntegerField(source="group_id")
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksUserDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    login = serializers.CharField()
    admin = serializers.BooleanField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.EmailField()
    role = serializers.IntegerField(source="role_id")
    group = serializers.IntegerField(source="group_id")
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksUserSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    login = serializers.CharField()
    admin = serializers.BooleanField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.EmailField()
    role = serializers.IntegerField(source="role_id")
    group = serializers.IntegerField(source="group_id")
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksUserCreateInputSerializer(serializers.Serializer):
    login = serializers.CharField()
    admin = serializers.BooleanField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.EmailField()
    role = serializers.IntegerField()
    group = serializers.IntegerField()


class TasksUserUpdateInputSerializer(serializers.Serializer):
    login = serializers.CharField()
    admin = serializers.BooleanField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.EmailField()
    role = serializers.IntegerField()
    group = serializers.IntegerField()


class TasksUserPartialUpdateInputSerializer(serializers.Serializer):
    login = serializers.CharField(required=False)
    admin = serializers.BooleanField(required=False)
    firstname = serializers.CharField(required=False)
    lastname = serializers.CharField(required=False)
    mail = serializers.EmailField(required=False)
    role = serializers.IntegerField(required=False)
    group = serializers.IntegerField(required=False)


class TasksUserFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    login = serializers.CharField()
    admin = serializers.BooleanField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.EmailField()
    role = serializers.IntegerField(source="role_id")
    group = serializers.IntegerField(source="group_id")
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class TasksUserFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    login = serializers.CharField(required=False)
    admin = serializers.BooleanField(required=False, allow_null=True)
    firstname = serializers.CharField(required=False)
    lastname = serializers.CharField(required=False)
    role = serializers.IntegerField(required=False)
    group = serializers.IntegerField(required=False)


class TasksUserStatsOutputSerializer(serializers.Serializer):
    role = serializers.IntegerField(source="role_id")
    count_users = serializers.IntegerField()
