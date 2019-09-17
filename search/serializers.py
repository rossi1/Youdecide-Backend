"'"
#from .models import SearchHistory, FailedSearchHistory
from rest_framework import serializers



"""

class SearchHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchHistory
        fields = '___all__'


class FailedSearchHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FailedSearchHistory
        fields = '__all__'


from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from polls.models import Poll
from .search_index import PollIndex

"""


from polls.models import Poll

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .document import PollDocument

class PollBookSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = PollDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'question',
            'slug',
            'expire_date',
            'pub_date',
            #'created_by'
        
        )
