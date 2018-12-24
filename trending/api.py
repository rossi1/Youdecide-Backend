from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from polls.models import Poll
from polls.serializers import PollSerializer


class PollTrendingAPIListView(APIView):
    """
    List all the trending instances
    """
    def get(self, request, format=None):
        poll = Poll.objects.order_by('vote')
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     serializer = PollSerializer(data=request.data)
    #     if serializer.is_valid():
    #         try:
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         except:
    #             return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
