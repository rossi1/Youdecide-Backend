import json
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied

from ipware import get_client_ip

from anonymous_user.models import AnonymousVoter
from .models import Poll, Choice, Vote, VoteCount
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from .utils import filter_votes, get_poll_votes_count


class AnonymousUserPermission(BasePermission):

    """Custom permission class to authenticate against AnonymousUser and stop double voting """
    
    def has_permission(self, request, view):
        
        poll_pk = view.kwargs['pk']
        print(poll_pk)

        if request.user.is_authenticated:
            if Vote.objects.filter(Q(poll=poll_pk), Q(voted_by=request.user)).exists():
                raise PermissionDenied('Double voting disallowed')
            return True

        ip_address, is_routable =  get_client_ip(request)# fetch anonymous_user current ip address
        
        if Vote.objects.filter(Q(poll=poll_pk), Q(anonymous_voter__ipaddress=ip_address)).exists():
            raise PermissionDenied('Double voting disallowed')
        return True


class PollCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Poll 
    serializer_class = PollSerializer


class PollList(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    

class PollDetail(generics.RetrieveAPIView):

    """custom response updates coming soon"""

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_url_kwarg = 'pk'

    
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, context=self.get_serializer_context())
        anonymous_voter_queryset = queryset.poll_vote.values('anonymous_voter')
        filter_votes_list = filter_votes(anonymous_voter_queryset)
        anonymous_user_votes = {'anonymous_user': filter_votes_list}
        registered_voter_queryset = queryset.poll_vote.values('voted_by')
        filter_votes_list =  filter_votes(registered_voter_queryset, is_anonymous=False)
        registered_user_votes = {'registered_user': filter_votes_list}
        update_serializer_data = serializer.data['choices'][0]['votes']
        update_serializer_data.append(anonymous_user_votes)
        update_serializer_data.append(registered_user_votes) 
        poll_count = get_poll_votes_count(queryset.pk)
        data= {'poll_count': poll_count.poll_vote_count.vote_count, 'poll': serializer.data}
        return Response(data)
        
    

class PollDelete(generics.RetrieveDestroyAPIView):
    pass


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    permission_classes = (
        AnonymousUserPermission,)
    serializer_class = VoteSerializer
    queryset = Vote

    def create(self, request, pk, choice_pk):
        data = {'choice': choice_pk, 'poll': pk}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        if request.user.is_authenticated:
            self.perform_create(serializer)
            count = self.get_poll_votes_count(data['poll'])
            votes = {'votes': serializer.data, 'vote_count': count.poll_vote_count.vote_count}
            return Response(votes, status=status.HTTP_201_CREATED)
        email_address = request.data.get('email', 'testing12@gmaiil.com')  # testing if the email wasn't passed in the
        # request data
        phone_number = request.data.get('phone_number', '0703699887') 
        username  = request.data.get('username')
        # the request data
        anonymous_ip, is_routable = get_client_ip(request)
        browsername= request.user_agent.browser.family 
        browserversion = request.user_agent.os.version_string
        operatingsystem = request.user_agent.os.family  
        devicename = request.user_agent.os.family
        anonymous_user = AnonymousVoter.objects.create(ipaddress=anonymous_ip,
        browsername=browsername, browserversion=browserversion, operatingsystem=operatingsystem,
        devicename=devicename, email_address=email_address, phone_number=phone_number, username=username
        
        )
        self.perform_create(serializer, anonymous_user)
        count = get_poll_votes_count(data['poll'])
        votes = {'votes': serializer.data, 'vote_count': count.poll_vote_count.vote_count}
        return Response(votes, status=status.HTTP_201_CREATED)

    def perform_create(self, instance, anonymous_user=''):
        if anonymous_user == '':
            instance.save(voted_by=self.request.user)
        else:
            instance.save(anonymous_voter=anonymous_user)

    
    
        

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
#
# from .models import Poll, Choice
# from .serializers import PollSerializer
#
#
# class PollList(APIView):
#
#     def get(self, request):
#         polls = Poll.objects.all()[:20]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)
#
#
# class PollDetail(APIView):
#
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)

# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
#
# from .models import Poll
#
# def polls_list(request):
#     MAX_OBJECTS = 20
#     polls = Poll.objects.all()[:MAX_OBJECTS]
#     data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
#     return JsonResponse(data)
#
#
# def polls_detail(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     data = {"results": {
#         "question": poll.question,
#         "created_by": poll.created_by.username,
#         "pub_date": poll.pub_date
#     }}
#     return JsonResponse(data)
