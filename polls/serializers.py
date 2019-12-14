import json
import os

from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from anonymous_user.models import AnonymousVoter
from .models import Poll, Choice, Vote
from .utils import cloudinary_upload_image, cloudinary_upload_video

from userprofile.models import BookMark, Likes


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('choice', 'poll')


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    audio = serializers.FileField(required=False)
    video = serializers.FileField(required=False)


    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'id', 'audio', 'video']
        

    def create(self, validated_data):
        try:
            audio = validated_data.pop('audio')
            upload_audio = cloudinary_upload_image(audio)
        except KeyError:
            try:
                video = validated_data.pop('video')
                upload_video = cloudinary_upload_video(video)
            except KeyError:
                return Choice.objects.create(**validated_data)
            else:
                return Choice.objects.create(choice_video=upload_video, **validated_data)

        else:
            return Choice.objects.create(choice_audio=upload_audio, **validated_data)

    

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
    
    def validate_choice_audio(self, value):
        if value.size > 5*1024*1024:
            raise serializers.ValidationError("Audio file too large ( > 5mb )")
        if not value.content_type in ["audio/mpeg", "audio/wav"]:
            raise serializers.ValidationError("Content-Type is not mpeg")
        if not os.path.splitext(value.name)[1] in [".mp3",".wav"]:
            raise serializers.ValidationError("Doesn't have proper extension")
        return value
        
    def validate_choice_video(self, value):
        if value.size > 5*1024*1024:
            raise serializers.ValidationError("Large file too large ( >54mb )")
        if value.content_type in ["video/mp4", "video/webm"]:
            raise serializers.ValidationError("Content-Type is not mpeg")
        if not os.path.splitext(value.name)[1] in [".mp4"]:
            raise serializers.ValidationError("Doesn't have proper extension")

            return value
        else:
            raise serializers.ValidationError("Couldn't read uploaded file")

    

class PollSerializer(serializers.ModelSerializer):
    
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    poller_username = serializers.SerializerMethodField()
    slug_field = serializers.SerializerMethodField()


    class Meta:
        model = Poll
        fields = ['id', 'pub_date',  'question', 'choices', 'poller_username', 'choice_type', 'expire_date', 'slug_field']

    def get_poller_username(self, instance):
        return instance.created_by.username

    def get_slug_field(self, instance):
        return instance.slug

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
            
            ret['poll_has_been_bookmarked'] =  poll_has_been_bookmarked
            ret['poll_has_been_liked'] =  poll_has_been_liked
    
        ret['total_likes'] = instance.poll_likes.all().count()
        ret['vote_count'] = instance.poll_vote.count()
        return ret

    