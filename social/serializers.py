from rest_framework import serializers
from .models import Follow


      
class FollowSerializer(serializers.ModelSerializer):
    """Follower Serializer"""
  

    class Meta:
        model = Follow
        fields = '__all__'


