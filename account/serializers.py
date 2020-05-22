from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError


from userprofile.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    user_image = serializers.SerializerMethodField()
    """UserProfile Serializer"""

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'place_of_work', 'position', 'about', 'user_image')

    def get_user_image(self, instance):
        try:
            return instance.image.url
        except AttributeError:
            return None


class UserSerializer(serializers.ModelSerializer):
    profile =  UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = validated_data.pop('profile')
        Profile.objects.create(user=user, **profile)
        return user
    
    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('A user with that email already exists.')
        return value

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('A user with that username already exists')

        return value
    


class AllUsersSerializer(serializers.ModelSerializer):
    """Serializer for User model having only the field required for all users"""

    class Meta:
        model = User
        # Note that id is non-updatable, therefore not required in the
        # read-only fields
        fields = ('id', 'username',)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=250)


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

    class Meta:
        model = User
        fields = ('old_password', 'new_password')
