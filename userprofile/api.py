from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from .models import BookMark
from userprofile.serializers import SingleUserSerializer, UserProfileSerializer, BookmarkSerializer
from rest_framework import generics


class SingleUserAPIDetailView(RetrieveUpdateAPIView):
    """
    Retrieve instance.
    /api/v1/users/<id> url path
    """
    serializer_class = SingleUserSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = SingleUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookMarkList(generics.ListCreateAPIView):
    """ get all the user bookmarks
    """
    queryset = BookMark.objects.all()
    serializer_class = BookmarkSerializer

