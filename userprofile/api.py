from collections import OrderedDict

from django.http import Http404
from django.contrib.auth.models import User
from django.db.models import F, Count

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated


from social.models import Follow
from polls.models import Poll

from .models import BookMark, Likes,Profile
from userprofile.serializers import SingleUserSerializer, UserProfileSerializer, \
    BookmarkSerializer,LikeSerializer



class UpdateUserProfiileAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset =Profile
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.queryset.objects.get(user=self.request.user)


class SingleUserAPIDetailView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    """
    Retrieve instance.
    /api/v1/users/<id> url path
    """
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'pk'
    serializer_class = SingleUserSerializer
    queryset  = User    


    def get(self, request, pk, format=None):
        user_info = OrderedDict()
        user = self.get_object()
        serializer = SingleUserSerializer(user, context=self.get_serializer_context())
        poll = Poll.objects.filter(created_by=user).values('question', 'pub_date', 'pk')
       
        like = Likes.objects.filter(user=user).values('like_date', question=F('poll__question'), 
        pk=F('poll__pk'), pub_date=F('poll__pub_date'))

        user_info['profile_data'] = UserProfileSerializer(user, context=self.get_serializer_context()).data
        user_info['user'] = serializer.data
        user_info['followers']= Follow.objects.get_followers(user) 
        user_info['followed'] = Follow.objects.get_followings(user)
        user_info['polls'] = poll
        user_info['likes'] =like 
        return Response(user_info, status=status.HTTP_200_OK)


    def update(self, request, *args, **kwargs):
        """extra validation here to prevent maclious activities"""

        if kwargs['pk'] == request.user.pk:
            return super().update(request, *args, **kwargs)
        return Response({'status': 'Failed', 'message': 'Hey there you cant do that'}, status=status.HTTP_403_FORBIDDEN)


class BookMarkAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    """ get all the user bookmarks
    """
    queryset = BookMark.objects.all()
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).all()
   

class LikesAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).all()
    
class DeleteBookMarkedAPIView(generics.DestroyAPIView):
    queryset = BookMark
    serializer_class = BookmarkSerializer
    lookup_field = 'pk'

class DeleteLikesAPIView(generics.DestroyAPIView):
    queryset = Likes
    serializer_class = LikeSerializer
    lookup_field = 'pk'

   

