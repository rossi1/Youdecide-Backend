from .models import SearchHistory, FailedSearchHistory
from rest_framework import serializers


class SearchHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchHistory
        fields = '___all__'


class FailedSearchHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FailedSearchHistory
        fields = '__all__'


