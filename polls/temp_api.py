# from rest_framework.views import APIView
# from rest_framework.generics import RetrieveUpdateAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404, JsonResponse
# from polls.models import Poll, Vote, Choices
# from polls.serializers import PollSerializer, VoteSerializer, ChoiceSerializer
# import json
# import base64
# import random
#
#
# class PollAPIListView(APIView):
#     """
#     List all the Poll instances, or create a new Poll instance.
#     """
#     def get(self, request, format=None):
#         poll = Poll.objects.all()
#         serializer = PollSerializer(poll, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         serializer = PollSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except:
#                 return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PollAPIDetailView(RetrieveUpdateAPIView):
#     """
#     Retrieve, update or delete a given Poll instance.
#     """
#     serializer_class = PollSerializer
#
#     def get_object(self, pk):
#         try:
#             return Poll.objects.get(pk=pk)
#         except Poll.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         poll = self.get_object(pk)
#         serializer = PollSerializer(poll)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk, format=None):
#         poll = self.get_object(pk)
#         serializer = PollSerializer(poll, data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except:
#                 return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         poll = self.get_object(pk)
#         poll.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class VoteAPIListView(APIView):
#     """
#     List all the Votes instances, or create a new Votes instance.
#     """
#     def get(self, request, format=None):
#         vote = Vote.objects.all()
#         serializer = VoteSerializer(vote, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         serializer = VoteSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except:
#                 return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class VotesAPIView(RetrieveUpdateAPIView):
#     """
#     Retrieve, update or delete a given Vote instance.
#     """
#     serializer_class = VoteSerializer
#
#     def get_object(self, pk):
#         try:
#             return Vote.objects.get(pk=pk)
#         except Vote.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         vote = self.get_object(pk)
#         serializer = VoteSerializer(vote)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk, format=None):
#         vote = self.get_object(pk)
#         vote.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class SinlgePOllAPIView(RetrieveUpdateAPIView):
#     """
#     Retrieve, update or delete a given Choice instance.
#     """
#
#     # serializer_class = VoteSerializer
#
#     def get_object(self, pk):
#         try:
#             return Poll.objects.get(pk=pk)
#         except Poll.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         results = Poll.objects.filter(pk=pk).values('question', 'choices__choice_text', 'created_by__username',
#                                                    'pub_date', 'expire_date', 'choice_type','slug')
#         data = dict()
#         data['question'] = results[0]['question']
#         data['choice_type'] = results[0]['choice_type']
#         data['choices'] = []
#         for query in results:
#             data['choices'].append(query['choices__choice_text'])
#         data['created_by'] = results[0]['created_by__username']
#         data['pub_date'] = str(results[0]['pub_date'])
#         data['expire_date'] = str(results[0]['expire_date'])
#         data['slug'] = str(results[0]['slug'])
#         print(data)
#         return JsonResponse(data)  # JsonResponse({'results': list(results)})
#         #  Response(data, status=status.HTTP_200_OK)
#
#
# class ChoiceAPIView(RetrieveUpdateAPIView):
#     """
#     Retrieve, update or delete a given Choice instance.
#     """
#     serializer_class = VoteSerializer
#
#     def get_object(self, pk):
#         try:
#             return Choices.objects.get(pk=pk)
#         except Choices.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         choice = self.get_object(pk)
#         serializer = ChoiceSerializer(choice)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk, format=None):
#         vote = self.get_object(pk)
#         vote.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # set the width of the key
# default_size = 2
#
#
# def make_token(mysize=default_size):
#     '''Computes an access token to an api randomly none deterministic.
#     this test should always fail becuase is random value generation
#     : param size: the width of the bytes
#     : returns: a random token
#     '''
#     random_seed = random.SystemRandom()
#     token_bytes = bytes(random_seed.randrange(0, 256) for index in range(18 * mysize))
#     token_base64 = base64.urlsafe_b64encode(token_bytes)
#     token_string = token_base64.decode('ascii')
#     return token_string
#
#
# def getPoll(pk):
#     results = Poll.objects.filter(pk=pk).values('question', 'choices__choice_text', 'created_by__username',
#                                                    'pub_date', 'expire_date', 'choice_type', 'slug')
#     data = dict()
#     data['question'] = results[0]['question']
#     data['choices'] = []
#     for query in results:
#         data['choices'].append(query['choices__choice_text'])
#     data['created_by'] = results[0]['created_by__username']
#     data['pub_date'] = str(results[0]['pub_date'])
#     data['expire_date'] = str(results[0]['expire_date'])
#     data['choice_type'] = results[0]['choice_type']
#     data['slug'] = str(results[0]['slug'])
#     return data