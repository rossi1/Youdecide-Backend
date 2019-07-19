
"""
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
)
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

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
    ]
    # Define search fields
    search_fields = (

        'question',
        'created_by',
        'pub_date'
    )
    
    # Define filtering fields
    filter_fields = {
        'id': None,
        'question': 'question.raw',
        'created_by': 'created_by.raw',
        'pub_date': 'pub_date.raw',
    }
    # Define ordering fields
    ordering_fields = {
        'id': None,
        'question': None,
        'created_by': None,
        'pub_date': None,
    }
    
    # Specify default ordering
    ordering = ('pub_date',)
"""
