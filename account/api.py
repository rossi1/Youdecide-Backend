import json

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from youdecide import settings
from userprofile import models, serializers

from .serializers import UserSerializer, AllUsersSerializer, ChangePasswordSerializer



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


@method_decorator(csrf_exempt, name='post')
class UserCreate(generics.CreateAPIView):
    """For /api/v1/users/signup url path"""
    # authentication_classes = ()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = ()
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     new_user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'),)
    #     if new_user is not None:
    #         if new_user.is_active:
    #             login(request, new_user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginView(APIView):
    """For /api/v1/users/login url path"""
    permission_classes = ()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request,):
        username = None
        if request.data.get("username") is not None:
            username = request.data.get("username")
        else:
            username = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        #token, created = Token.objects.get_or_create(user=user)
        if user:
            # user = json.dumps(user)
            token = self.get_tokens_for_user(user)

            return Response({"token": token})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_tokens_for_user(user):
        "custom method to create new refresh and access tokens for the given user"

        refresh = RefreshToken.for_user(user)
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }


class IsOwner(permissions.BasePermission):
    """
    Custom of class IsOwnerOrReadOnly(permissions.BasePermission)
    That an APIexception is raised instead
    We do not want a ReadOnly
    """

    def has_object_permission(self, request, view, obj):

        # First check if authentication is True
        permission_classes = (permissions.IsAuthenticated, )
        # Instance is the user
        return obj.id == request.user.id


class UserListAPIView(generics.ListAPIView):
    """For /api/v1/users/ url path"""

    queryset = User.objects.all()
    serializer_class = AllUsersSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    """For /api/v1/users/<id> url path"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner, )


class UserRegisterAPIView(generics.CreateAPIView):
    """For /api/v1/auth/register url path"""
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserLogoutAPIView(generics.UpdateAPIView):
#     """For /api/v1/users/logout url path"""
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsOwner, )

class Logout(APIView):
    """For /api/v1/users/logout url path"""

    def get(self, request, format=None):
        # simply delete the token to force a login
        if request.auth:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        return HttpResponseRedirect(settings.LOGIN_URL)


class ChangePasswordView(generics.UpdateAPIView):
    """
    For /api/v1/users/change-password url path
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserFollowAPIView(generics.CreateAPIView):
#     """
#     For api/v1/users/<>/follow/ url path
#     To enable user to add or remove those that they follow
#     """
#
#     serializer_class = UserFollowSerializer
#
#     def get_queryset(self):
#         to_be_followed = User.objects.filter(id=self.kwargs['pk']).first()
#         return to_be_followed
#
#     def perform_create(self, serializer):
#         self.user = User.objects.filter(id=self.request.user.id).first()
#         try:
#             models.Follow.objects.create(
#                 follower=self.user, followed=self.get_queryset())
#             return {"message":
#                     "You have followed user'{}'".format(
#                         self.get_queryset())}, 201
#         except:
#             raise serializers.serializers.ValidationError(
#                 'You have already followed this person')

