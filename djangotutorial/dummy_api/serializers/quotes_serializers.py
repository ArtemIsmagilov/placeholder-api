from rest_framework import serializers


class QuoteListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class QuoteDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class QuoteSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class QuoteCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()


class QuoteUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()


class QuotePartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)


class QuoteFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class QuoteFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)