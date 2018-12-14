from .models import Poll, Choices, Vote, PollDuration
from rest_framework import serializers


class VoteSerializer(serializers.ModelSerializer):
    # vote_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('vote_count',)


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choices
        fields = '__all__'


class PollDurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollDuration
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    # poll_duration = PollDurationSerializer(many=True, required=False)

    class Meta:
        model = Poll
        # fields = ('question', 'created_by', 'pub_date')
        fields = '__all__'
        read_only_fields = ('slug', 'pub_date')





