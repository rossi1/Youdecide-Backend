from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from polls.models import Poll
from polls.serializers import PollSerializer


class PollTrendingAPIListView(APIView):
    """
    List all the trending poll instances
    api/v1/trending/polls
    """
    def get(self, request, format=None):
        poll = Poll.objects.order_by('vote')
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

