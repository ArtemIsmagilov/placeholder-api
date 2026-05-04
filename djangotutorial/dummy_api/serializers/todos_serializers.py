from rest_framework import serializers


class DummyTodoListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class DummyTodoDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class DummyTodoSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class DummyTodoCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField()


class DummyTodoUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField()


class DummyTodoPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    user = serializers.IntegerField(required=False)


class DummyTodoFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class DummyTodoFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    user = serializers.IntegerField(required=False)


class DummyTodoStatsOutputSerializer(serializers.Serializer):
    user = serializers.IntegerField(source="user_id")
    count_todos = serializers.IntegerField()
    count_completed = serializers.IntegerField()
    count_uncompleted = serializers.IntegerField()
