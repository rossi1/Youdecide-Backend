import json
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from anonymous_user.models import AnonymousVoter
from .models import Poll, Choice, Vote

from userprofile.models import BookMark, Likes, Share



class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('choice', 'poll')


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'id']

    def create(self, **validated_data):
        pass
    

    def to_representation(self, instance):
        from .utils import filter_votes

        ret = super(ChoiceSerializer, self).to_representation(instance)
    
        try:
            choice_vote_count = instance.votes.all().count()
        except AttributeError:
            return ret
        else:
            ret['choice_vote_count'] = choice_vote_count

        ret['registered_voter'] = filter_votes(instance.votes.values('voted_by__username'))
        ret['anonymous_voter'] = filter_votes(instance.votes.values('anonymous_voter__username'))
       
        return ret

class PollSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method == "GET":
            try:
                self.Meta.fields.append('expire_date')
                self.Meta.fields.append('slug')
            except ValueError:
                pass

            
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    poller_username = serializers.SerializerMethodField()
  
  
    class Meta:
        model = Poll
        fields = ['id', 'created_by', 'pub_date',  'question', 'choices', 'poller_username']

    def to_representation(self, instance):
        ret = super(PollSerializer, self).to_representation(instance)
        request = self.context['request']
        poll_has_been_bookmarked = False
        poll_has_been_liked = False
        poll_has_been_shared = False
        if request.user.is_authenticated:
            if BookMark.objects.filter(user=request.user, poll=instance).exists():
                poll_has_been_bookmarked = True
            if Likes.objects.filter(user=request.user, poll=instance).exists():
                poll_has_been_liked = True

            if Share.objects.filter(user=request.user, poll=instance).exists():
                poll_has_been_shared = True
        
        ret['poll_has_been_bookmarked'] =  poll_has_been_bookmarked
        ret['poll_has_been_liked'] =  poll_has_been_liked
        ret['poll_has_been_shared'] =  poll_has_been_shared
        ret['total_likes'] = instance.poll_likes.all().count()
        ret['total_shares'] = instance.poll_share.all().count()
        ret['vote_count'] = instance.poll_vote.count()
        return ret

    def get_poller_username(self, instance):
        
        return instance.created_by.username
