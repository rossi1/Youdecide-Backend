from .models import SearchHistory, FailedSearchHistory
from rest_framework import serializers

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .document import PollDocument


class SearchHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchHistory
        fields = '___all__'


class FailedSearchHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FailedSearchHistory
        fields = '__all__'


class PollDocumentSerializer(DocumentSerializer):
    """Serializer for Poll document."""

    class Meta(object):
        # = Poll
        document = PollDocument
        """Meta options."""
        fields = (
            'id',
            'question',
            'pub_date',
            )

