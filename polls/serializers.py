import json


from django.contrib.auth.models import User



from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Poll, Choice, Vote, VoteCount





class VoteSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Vote
        fields = ('choice', 'poll')


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    
    
    

    class Meta:
        model = Poll
        fields = '__all__'


