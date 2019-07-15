import json
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from anonymous_user.models import AnonymousVoter
from .models import Poll, Choice, Vote, VoteCount





class VoteSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        """ Overriding Init method to return custom model fields """
        super(VoteSerializer, self).__init__(*args, **kwargs)
       

    class Meta:
        model = Vote
        fields = ('choice', 'poll')

    



class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


    
    def to_representation(self, instance):
        ret = super(ChoiceSerializer, self).to_representation(instance)
    
        try:
            choice_vote_count = instance.votes.all().count()
        except AttributeError:
            return ret
        else:
            ret['choice_vote_count'] = choice_vote_count

        return ret
    
    
    


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'


