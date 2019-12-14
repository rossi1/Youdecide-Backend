from rest_framework import serializers

from social.models import Follow

from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

        #user = self.context['request'].user
        