from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from polls.models import Poll
from polls.serializers import PollSerializer


class PollFeedAPIListView(APIView):
    """
    List all the Poll instances and return as the feeds.
    """
    def get(self, request, format=None):
        poll = Poll.objects.all()
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PollAPIDetailView(RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a given Poll instance.
    """
    serializer_class = PollSerializer

    def get_object(self, pk):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        poll = self.get_object(pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)