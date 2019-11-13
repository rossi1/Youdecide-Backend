import json

from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission


from ipware import get_client_ip

from account.permissions import IsOwner
from anonymous_user.models import AnonymousVoter

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from .utils import filter_votes
from .permissions import AnonymousUserPermission



class PollCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Poll 
    serializer_class = PollSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PollList(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    

class PollDetail(generics.RetrieveUpdateAPIView):
    queryset = Poll.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = PollSerializer
    lookup_url_kwarg = 'pk'
    
    def retrieve(self, request, *arg, **kwargs):
        return super().retrieve(request, *arg, **kwargs)

    def update(self, request, *args, **kwargs):
       
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        if not request.user.is_authenticated:
            return Response({'message':'Unable to process request'}, status=status.HTTP_403_FORBIDDEN)
        if instance.created_by != request.user:
            return Response({'message':'Unable to process request'}, status=status.HTTP_403_FORBIDDEN)
        if instance.poll_vote.count() > 0:
        
            return Response({'message':'Poll ongoing unable to edit poll '}, status=status.HTTP_403_FORBIDDEN)
        self.perform_update(serializer)
        return Response(serializer.data)
            
       

class PollDelete(generics.DestroyAPIView):
    queryset = Poll
    serializer_class = PollSerializer
    lookup_url_kwarg = 'pk'
    permission_classes = (IsAuthenticated, IsOwner)
    

class ChoiceList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):
        poll = generics.get_object_or_404(Poll, id=self.kwargs["pk"])
        serializer.save(poll=poll)

        
class ChoiceDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = ChoiceSerializer
    lookup_url_kwarg = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.object()
        if instance.votes().count() > 0:
            return Response({'message':'Poll ongoing unable to delete poll choice '}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)


class ChoiceEdit(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = ChoiceSerializer
    lookup_url_kwarg = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.votes.count() > 0:
            return Response({'message':'Poll ongoing unable to edit poll choice '}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        email_address = request.data.get('email', 'emma@gmaiil.com')
        phone_number = request.data.get('phone_number', '07036999887') 
        username  = request.data.get('username', 'jmax')
        anonymous_ip, is_routable = get_client_ip(request)
        browsername= request.user_agent.browser.family 
        browserversion = request.user_agent.os.version_string
        operatingsystem = request.user_agent.os.family  
        devicename = request.user_agent.os.family

        try:
            anonymous_voter = AnonymousVoter.objects.get(ipaddress=anonymous_ip)
        except AnonymousVoter.DoesNotExist:
            anonymous_user = AnonymousVoter.objects.create(ipaddress=anonymous_ip,
            browsername=browsername, browserversion=browserversion, operatingsystem=operatingsystem,
            devicename=devicename, email_address=email_address, phone_number=phone_number, username=username)
            self.perform_create(serializer, anonymous_user)
        else:
            self.perform_create(serializer, anonymous_voter)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, instance, anonymous_user=''):
        if anonymous_user == '':
            instance.save(voted_by=self.request.user)
        else:
            instance.save(anonymous_voter=anonymous_user)