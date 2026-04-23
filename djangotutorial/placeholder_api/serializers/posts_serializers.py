from rest_framework import serializers


class PostListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PostDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PostSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PostCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField()


class PostUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField()


class PostPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class PostFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PostFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class PostStatsOutputSerializer(serializers.Serializer):
    user = serializers.IntegerField(source="user_id")
    count_posts = serializers.IntegerField()
