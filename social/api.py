from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Follow
from .serializers import FollowSerializer

class FollowUserAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer
    queryset = Follow
    

class ListFollowersAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer
    queryset = Follow

    def get_queryset(self):
        return self.queryset.objects.get_followers(self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(queryset)
        return Response(queryset)


class ListFollowingAPIView(ListFollowersAPIView):

    def get_queryset(self):
        return self.queryset.objects.get_followings(self.request.user)


class UnfollowAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Follow
    serializer_class = FollowSerializer
    lookup_field = 'id'

    




    
