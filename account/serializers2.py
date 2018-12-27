from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from account.models import Users, UserType


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class CustomUserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #         required=True,
    #         validators=[UniqueValidator(queryset=Users.objects.all())]
    #         )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=Users.objects.all())]
            )
    password = serializers.CharField(min_length=8)
    createddate = serializers.DateTimeField(required=False)
    lastupdated = serializers.DateTimeField(required=False)

    # def create(self, validated_data):
    #     user = Users.objects.create(validated_data['username'],
    #          validated_data['password'], validated_data['userstatus'])
    #     # , validated_data['createddate'],validated_data['lastupdated'])
    #     return user

    def create(self, validated_data):
        obj = Users.objects.create(**validated_data)
        # obj.save(foo=validated_data['foo'])
        obj.save()
        return obj

    class Meta:
        model = Users
        fields = ('users_id', 'username', 'password', 'userstatus', 'createddate', 'lastupdated')


class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserType
        fields = ('user_type_id', 'title', 'description', 'createddate', 'lastupdated')