from django.contrib.auth.models import User
from django.core import serializers
from rest_framework import serializers
from social.models import Follow

from .models import BookMark, Likes, Profile


class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfile Serializer"""

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'place_of_work', 'position', 'about', 'image')


class SingleUserSerializer(serializers.ModelSerializer):
    """Serializer for User model having only the field required for all users"""

    follow_status = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        # Note that id is non-updatable, therefore not required in the
        # read-only fields
        fields = ('id', 'username', 'follow_status')

    def get_follow_status(self, instance):
        follow_stat = {}
        request = self.context.get('request',  None)
        if request is not None:
            user = request.user
            if user.is_authenticated:
                follower_list = Follow.objects.get_followers_list(instance)
                if instance == user:
                    return follow_stat

                if user.pk in follower_list:
                    follow_stat['following_user'] = True
                else:
                    follow_stat['following_user'] = False

                following_list = Follow.objects.get_followings_list(instance)

                if user.pk in following_list:
                    follow_stat['user_following'] = True
                else:
                    follow_stat['user_following'] = False
                
        return follow_stat



class BookmarkSerializer(serializers.ModelSerializer):
    poll_question_text = serializers.SerializerMethodField()
    
    def get_poll_question_text(self, instance):
        return str(instance.poll)

    class Meta:
        model = BookMark
        fields = ('id', 'poll', 'user', 'created', 'poll_question_text')



class LikeSerializer(serializers.ModelSerializer):
    poll_question_text = serializers.SerializerMethodField()

    def get_poll_question_text(self, instance):
        return str(instance.poll)

    class Meta:
        model = Likes
        fields = ('id', 'poll', 'user', 'like_date',  'poll_question_text')
