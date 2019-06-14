from django.db.models import Q

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied


from ipware import get_client_ip

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.views import BaseDocumentViewSet


from anonymous_user.models import AnonymousVoter
from .models import Poll, Choice, Vote
from .document import PollDocument
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, PollDocumentSerializer


class AnonymousUserPermission(BasePermission):

    """Custom permission class to authenticate against AnonymousUser and stop double voting """
    
    def has_permission(self, request, view):
        poll_pk = request.query_params.get('poll_pk')
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
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        email_address = request.data.get('email', 'testing12@gmaiil.com') # testing if the email wasn't passed in the request data
        phone_number = request.data.get('phone_number', '0703699887')# testing if the phone_number wasn't passed in the request data
        anonymous_ip, is_routable = get_client_ip(request)
        browsername= request.user_agent.browser.family 
        browserversion = request.user_agent.os.version_string
        operatingsystem = request.user_agent.os.family  
        devicename = request.user_agent.os.family 


        anonymous_user = AnonymousVoter.objects.create(ipaddress=anonymous_ip,
        browsername=browsername, browserversion=browserversion, operatingsystem=operatingsystem,
        devicename=devicename, email_address=email_address, phone_number=phone_number
        
        )
        self.perform_create(serializer, anonymous_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, instance, anonymous_user=''):
        if anonymous_user == '':
            instance.save(voted_by=self.request.user)
        else:
            instance.save(anonymous_voter=anonymous_user)

class PollDocumentView(BaseDocumentViewSet):
    """The PollDocument view."""

    document = PollDocument
    serializer_class = PollDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'question',
        'created_by',
        'pub_date'
    )
    """
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
    """
    # Specify default ordering
    ordering = ('id', 'pub_date',)
    
         
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
