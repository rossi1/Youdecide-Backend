import json


from django.contrib.auth.models import User

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .document import PollDocument

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Poll, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        exclude = ('voted_by', 'anonymous_voter')


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


class PollDocumentSerializer(DocumentSerializer):
    """Serializer for Poll document."""

    class Meta(object):
        # = Poll
        document = PollDocument
        
        """Meta options."""

        
        fields = (
            'question',
            'pub_date',
            'created_by'
        )