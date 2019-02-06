from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from polls.models import Poll
from polls.serializers import PollSerializer


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