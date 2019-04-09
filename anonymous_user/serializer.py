from rest_framework import serializers
from anonymous_user.models import AnonymousVoter
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password


class AnonymousVoterSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnonymousVoter
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
