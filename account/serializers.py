from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class AllUsersSerializer(serializers.ModelSerializer):
    """Serializer for User model having only the field required for all users"""

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the
        # read-only fields
        fields = ('id', 'username',)
#
# class CustomUserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(
#             validators=[UniqueValidator(queryset=Users.objects.all())]
#             )
#     password = serializers.CharField(min_length=8)
#     createddate = serializers.DateTimeField(required=False)
#     lastupdated = serializers.DateTimeField(required=False)
#
#     def create(self, validated_data):
#         obj = Users.objects.create(**validated_data)
#         # obj.save(foo=validated_data['foo'])
#         obj.save()
#         return obj
#
#     class Meta:
#         model = Users
#         fields = ('users_id', 'username', 'password', 'userstatus', 'createddate', 'lastupdated')
#
#
# class UserTypeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = UserType
#         fields = ('user_type_id', 'title', 'description', 'createddate', 'lastupdated')