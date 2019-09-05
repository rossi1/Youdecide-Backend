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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['follower'] == serializer.validated_data['following']:
            return Response({'status': 'failed', 'message': 'User cant follow itself'}, \
                status=status.HTTP_400_BAD_REQUEST)
        
       
        create = super().create(request, *args, **kwargs)
            
        return create
    

    def perform_create(self, serializer):
        try:
            serializer.save()
        except:
            raise ValidationError('User already followed')
            

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

    




    
