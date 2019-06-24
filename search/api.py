from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


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
from .document import PollDocument

from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet


from polls.models import Poll
from polls.serializers import PollSerializer
from search.serializers import SearchHistorySerializer, FailedSearchHistorySerializer, PollDocumentSerializer
from search.models import SearchHistory, FailedSearchHistory
from account.api import CsrfExemptSessionAuthentication




class SearchPollAPIListView(APIView):
    """
    List all the trending instances
    """
    def get(self, request, format=None):
        poll = Poll.objects.order_by('vote')
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchResultList(generics.ListAPIView):
    serializer_class = PollSerializer

    def get_queryset(self):
        """
        This view should return a list of all the polls for
        the user as determined by the username portion of the URL.
        """
        question = self.kwargs['question']
        user = self.request.user
        print(question)
        return Poll.objects.filter(question=question)

    def get(self, request, question, format=None):
        poll = self.get_queryset()
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchPollHistoriesAPIListView(APIView):
    """
    List all the poll searches by a user instances
    """
    permission_classes = ()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, format=None):
        poll = Poll.objects.order_by('vote')
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchPollHistoryAPIDetailView(RetrieveUpdateAPIView):
    """
    Retrieve a given poll search history instance.
    """
    serializer_class = SearchHistorySerializer
    permission_classes = ()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_object(self, pk):
        try:
            return SearchHistory.objects.get(pk=pk)
        except SearchHistory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        poll_search_history = self.get_object(pk)
        serializer = SearchHistorySerializer(poll_search_history)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FailedSearchesAPIListView(APIView):
    """
    List all failed searches for creation of future polls with highest failed searches
    """
    queryset = FailedSearchHistory.objects.all()
    serializer_class = FailedSearchHistorySerializer

    def get(self, request, format=None):
        failed_searches = FailedSearchHistory.objects.all()
        serializer = FailedSearchHistorySerializer(failed_searches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





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
    ordering = ('id', 'pub_date',)




