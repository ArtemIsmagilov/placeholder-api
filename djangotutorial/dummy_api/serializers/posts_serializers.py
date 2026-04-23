from rest_framework import serializers


class PostListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class PostDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class PostSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class PostCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField()


class PostUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField()


class PostPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    tags = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    dislikes = serializers.IntegerField(required=False)
    views = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class PostFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    user = serializers.IntegerField(source="user_id")


class PostFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    tags = serializers.CharField(required=False)
    likes = serializers.IntegerField(required=False)
    dislikes = serializers.IntegerField(required=False)
    views = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)


class PostStatsOutputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    count_posts = serializers.IntegerField()
    sum_views = serializers.IntegerField()
    sum_likes = serializers.IntegerField()
    sum_dislikes = serializers.IntegerField()
