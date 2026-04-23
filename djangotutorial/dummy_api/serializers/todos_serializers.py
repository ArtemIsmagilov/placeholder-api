from rest_framework import serializers


class TodoListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class TodoDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class TodoSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class TodoCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField()


class TodoUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField()


class TodoPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    user = serializers.IntegerField(required=False)


class TodoFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class TodoFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    user = serializers.IntegerField(required=False)


class TodosStatsOutputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    count_todos = serializers.IntegerField()
    count_completed = serializers.IntegerField()
    count_uncompleted = serializers.IntegerField()
