import json
import os

from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

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

    def validate_poll(self, instance):
        if self.context['request'].user.is_authenticated:
            if instance.created_by.id == self.context['request'].user:
                raise serializers.ValidationError("User cant vote on its poll")
        if instance.expire_date == timezone.now().date() or instance.expire_date <= timezone.now().date():
            raise serializers.ValidationError("Poll Ended, Unable to vote") 
        return instance

class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    votes = VoteSerializer(many=True, required=False, read_only=True)
    audio = serializers.FileField(required=False)
    video = serializers.FileField(required=False)


    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes',  'audio', 'video']
        

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
    choices = ChoiceSerializer(many=True, required=False)
    poller_username = serializers.SerializerMethodField()
    poller_username_id = serializers.SerializerMethodField()
    slug_field = serializers.SerializerMethodField()
    poll_has_expired = serializers.SerializerMethodField()
    poller_image = serializers.SerializerMethodField()


    class Meta:
        model = Poll
        fields = ['id', 'pub_date',  'question', 'choices', 'poller_username', 'choice_type', 'expire_date', 'slug_field', 'poller_username_id', 'poll_has_expired', 'poller_image']

    def get_poller_username(self, instance):
        return instance.created_by.username

    def get_poll_has_expired(self, instance):
        return instance.expire_date == timezone.now().date() or timezone.now().date() < instance.expire_date
    def get_poller_username_id(self, instance):
        return instance.created_by.id

    def get_poller_image(self, instance):
        try:
            return instance.created_by.profile.image.url
        except AttributeError:
            return None

    def get_slug_field(self, instance):
        return instance.slug

    def create(self, validated_data):
        choices = validated_data.pop('choices', None)
        poll = Poll.objects.create(**validated_data)
       

        if choices is not None:
            for choice in choices:
                Choice.objects.create(poll=poll, **choice)

        return poll

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.expire_date = validated_data.get('expire_date', instance.expire_date)
        instance.choice_type = validated_data.get('choice_type', instance.choice_type)
        instance.save()
        poll_choices = validated_data.get('choices', None)
        if poll_choices is not None:
            for choices in poll_choices:
                try:
                    choice = Choice.objects.get(poll=instance, id=choices.get('id'))
                   
                    if choice.votes.count() > 0:
                        raise serializers.ValidationError('Poll ongoing unable to edit poll choice ')
                    choice.choice_text = choices.get('choice_text', choice.choice_text)
                    choice.choice_audio = choices.get('choice_audio', choice.choice_audio)
                    choice.choice_video = choices.get('choice_video', choice.choice_video)
                except Choice.DoesNotExist:
                    pass

        return instance
        


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

    