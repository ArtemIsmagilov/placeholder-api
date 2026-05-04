from rest_framework import serializers


class PlaceholderPostListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderPostDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderPostSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderPostCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField()


class PlaceholderPostUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField()


class PlaceholderPostPartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class PlaceholderPostFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.IntegerField(source="user_id")


class PlaceholderPostFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)


class PlaceholderPostStatsOutputSerializer(serializers.Serializer):
    user = serializers.IntegerField(source="user_id")
    count_posts = serializers.IntegerField()
