from django.db.models import Q

from rest_framework import serializers
from .models import Follow


      
class FollowSerializer(serializers.ModelSerializer):
    """Follower Serializer"""
  

    class Meta:
        model = Follow
        fields = '__all__'

    def validate(self, attrs):
        cleaned_data = super(FollowSerializer, self).validate(attrs)
        if Follow.objects.filter(Q(follower=cleaned_data['follower']), Q(following=cleaned_data['following'])).exists():
            raise serializers.ValidationError("User already followed")

        if cleaned_data['follower'] == cleaned_data['following']:
            raise serializers.ValidationError("User cant follow yourself")

        return cleaned_data
            


