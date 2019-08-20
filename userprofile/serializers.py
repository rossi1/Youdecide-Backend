from django.contrib.auth.models import User
from django.core import serializers

from rest_framework import serializers

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
    
    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the
        # read-only fields
        fields = ('id', 'username',)


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

    


