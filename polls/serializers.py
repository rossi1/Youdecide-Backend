from .models import Poll, Choices
# from votes.models import Vote
from rest_framework import serializers


# class VoteSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Vote
#         fields = '__all__'
#
#
# class ChoiceSerializer(serializers.ModelSerializer):
#     votes = VoteSerializer(many=True, required=False)
#
#     class Meta:
#         model = Choice
#         fields = '__all__'
#
#
# class PollSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True, required=False)
#
#     class Meta:
#         model = Poll
#         fields = '__all__'

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('question', 'created_by', 'pub_date')


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choices
        fields = ('poll', 'choice_text')


