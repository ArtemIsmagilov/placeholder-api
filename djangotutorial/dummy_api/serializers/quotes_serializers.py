from rest_framework import serializers


class DummyQuoteListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class DummyQuoteDetailOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class DummyQuoteSearchOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class DummyQuoteCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()


class DummyQuoteUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()


class DummyQuotePartialUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)


class DummyQuoteFilterOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()


class DummyQuoteFilterInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)


class DummyQuoteStatsOutputSerializer(serializers.Serializer):
    author = serializers.CharField()
    count_quotes = serializers.IntegerField()
