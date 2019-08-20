from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Max
from polls.models import Poll, Vote
from polls.serializers import PollSerializer, VoteSerializer

from social.models import Follow
from userprofile.models import Share, Likes


class PollTrendingAPIListView(APIView):
    """
    List all the trending poll instances
    api/v1/trending/polls
    
    """
    def get(self, request, format=None):
        poll = Vote.objects.all().annotate(Max('poll_id'))
        serializer = VoteSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PollFeed(APIView):

    def get(self, request, *args, **kwargs):
        followings = Follow.objects.get_followings_list(request.user)
        print(followings)
        followers = Follow.objects.get_followers_list(request.user)
        print(followers)
        follow_list = followings  + followers
        print(follow_list)
        polls = Poll.objects.filter(created_by__in=follow_list)
       
        serializer = PollSerializer(polls, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


