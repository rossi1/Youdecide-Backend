from .models import SearchHistory
from rest_framework import serializers


class SearchHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchHistory
        fields = '___all__'


