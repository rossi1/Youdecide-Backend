from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from polls.models import Poll
from polls.serializers import PollSerializer
from search.serializers import SearchHistorySerializer
from search.models import SearchHistory
from account.api import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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
        print(question)
        return Poll.objects.filter(question=question)

    def get(self, request, question, format=None):
        poll = self.get_queryset()
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='get')
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


@method_decorator(csrf_exempt, name='get')
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


