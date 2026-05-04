from rest_framework import serializers


class PlaceholderTodoListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderTodoDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderTodoSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderTodoCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField()


class PlaceholderTodoUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField()


class PlaceholderTodoPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    user = serializers.IntegerField(required=False)


class PlaceholderTodoFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    completed = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderTodoFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    user = serializers.IntegerField(required=False)


class PlaceholderTodoStatsOutputSerializer(serializers.Serializer):
    user = serializers.IntegerField(source="user_id")
    count_todos = serializers.IntegerField()
    count_completed = serializers.IntegerField()
    count_uncompleted = serializers.IntegerField()
