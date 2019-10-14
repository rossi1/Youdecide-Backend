
#from .models import SearchHistory, FailedSearchHistory
from rest_framework import serializers


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
