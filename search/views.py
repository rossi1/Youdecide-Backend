from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    CompoundSearchFilterBackend,
    SuggesterFilterBackend
)
#from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet

from polls.models import Poll
from polls.serializers import PollSerializer

from .document import PollDocument
from .serializers import PollDocumentSerializer

class PollDocumentSearchView(BaseDocumentViewSet):
    """The PollDocument view."""

    document = PollDocument
    queryset = Poll.objects.all()
    serializer_class = PollDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
        SuggesterFilterBackend
    ]
    # Define search fields
    search_fields = (

        'question',
        'pub_date'
    )
    
    # Define filtering fields
    filter_fields = {
        'id': None,
        'question': 'question.raw',
        'pub_date': 'pub_date.raw',
    }
    # Define ordering fields
    ordering_fields = {
        'id': None,
        'question': None,
        'pub_date': None,
    }

    suggester_fields = {
        'question_suggest': {
            'field': 'question.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 20,  
            },
        },
       
       
    }

    # Specify default ordering
    ordering = ('pub_date',)
