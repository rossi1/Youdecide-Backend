from django.db.models import Q
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied
from ipware import get_client_ip
from anonymous_user.models import AnonymousUserModel
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class AnonymousUserPermission(BasePermission):

    """Custom permission class to authenticate against AnonymousUser and stop double voting """
    
    def has_permission(self, request, view):
        poll_pk = request.query_params.get('poll_pk')

        if request.user.is_authenticated:
            if Vote.objects.filter(Q(poll=poll_pk), Q(voted_by=request.user)).exists():
                raise PermissionDenied('Double voting disallowed')
            return True

        ip_address, is_routable =  get_client_ip(request)# fetch anonymous_user current ip address
        
        if Vote.objects.filter(Q(poll=poll_pk), Q(anonymous_voter__user_ip=ip_address)).exists():
            raise PermissionDenied('Double voting disallowed')
        return True


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


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
        detect_anonymous_user, is_routable = get_client_ip(request)

        anonymous_user = AnonymousUserModel.objects.create(user_ip=detect_anonymous_user)
        self.perform_create(serializer, anonymous_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
