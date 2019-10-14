
from itertools import chain

from django.http import Http404
from django.db.models import Max, F

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from polls.models import Poll, Vote
from polls.serializers import PollSerializer, VoteSerializer

from social.models import Follow
from userprofile.models import  Likes


class PollTrendingAPIListView(APIView):
    permission_classes = (IsAuthenticated,)
    """
    List all the trending poll instances
    api/v1/trending/polls
    
    """
    def get(self, request, format=None):
        poll = Vote.objects.all().annotate(Max('poll_id')).values(question=F('poll__question'), pk=F('poll__pk')
        )
        serializer = VoteSerializer(poll, many=True)
        return Response(poll, status=status.HTTP_200_OK)


class PollFeed(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        followings = Follow.objects.get_followings_list(request.user)
        polls = Poll.objects.filter(created_by__in=followings).distinct('id', 'pub_date').all()
        serializer = PollSerializer(polls, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


