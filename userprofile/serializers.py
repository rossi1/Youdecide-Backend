from rest_framework import serializers

from .models import UserProfile2, Follow  # , Notification, Language


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


# class LanguageSerializer(serializers.ModelSerializer):
#     """Language Serializer"""
#
#     class Meta:
#         model = Language
#         fields = ('name',)
#
#
# class NotificationSerializer(serializers.ModelSerializer):
#     """Notification Serializer"""
#
#     class Meta:
#         model = Notification
#         fields = ('link', 'activity_type', 'read',
#                   'content', 'date_created')
#
#         read_only_fields = ('date_created', 'link', 'activity_type', 'content')
