from django.contrib.auth.models import User
from django.core import serializers

from rest_framework import serializers

from social.models import Follow

from .models import Profile, BookMark, Share, Likes




"""
class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ('follower', 'followed', 'date_of_follow')

        read_only_fields = ('date_of_follow', 'follower')

"""
class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfile Serializer"""


    class Meta:
        model = Profile
        fields = ('social_id', 'first_name', 'last_name', 'place_of_work', 'position', 'about')

   


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
    """ Serialize the bookmarks"""

    class Meta:
        model = BookMark
        fields = ('id', 'poll', 'user', 'created')


    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['poll_question_text'] = str(instance.poll)
        return ret


class ShareSerializer(serializers.ModelSerializer):
    """ Serialize the shared polls"""

    class Meta:
        model = Share
        fields = ('id', 'poll', 'user', 'share_date')
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['poll_question_text'] = str(instance.poll)
        return ret

class LikeSerializer(serializers.ModelSerializer):
    """ Serialize the liked polls"""

    class Meta:
        model = Likes
        fields = ('id', 'poll', 'user', 'like_date')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['poll_question_text'] = str(instance.poll)
        return ret

    


