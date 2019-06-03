from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile2, Follow, BookMark, Share


class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer"""

    class Meta:
        model = Follow
        fields = ('follower', 'followed', 'date_of_follow')

        read_only_fields = ('date_of_follow', 'follower')


class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfile Serializer"""

    class Meta:
        model = UserProfile2
        fields = ('first_name', 'last_name', 'place_of_work', 'position', 'about', 'github_username', 'frequency',
                  'followers', 'followings', 'languages')


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
        fields = '__all__'


class ShareSerializer(serializers.ModelSerializer):
    """ Serialize the shared polls"""

    class Meta:
        model = Share
        fields = '__all__'

