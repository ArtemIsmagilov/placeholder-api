from rest_framework import serializers


class TasksProfileTaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    subject = serializers.CharField()
    description = serializers.CharField()
    done_percent = serializers.IntegerField()


class TasksProfileNewsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.CharField()


class TasksProfileCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()


class TasksProfileUserInfoSerializer(serializers.Serializer):
    login = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    mail = serializers.EmailField()
    admin = serializers.BooleanField()


class TasksProfileOutputSerializer(serializers.Serializer):
    user_info = TasksProfileUserInfoSerializer()
    tasks = TasksProfileTaskSerializer(many=True)
    news = TasksProfileNewsSerializer(many=True)
    comments = TasksProfileCommentSerializer(many=True)
