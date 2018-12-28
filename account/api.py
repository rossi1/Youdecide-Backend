from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.views.generic import View


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = None
        if request.data.get("username") is not None:
            username = request.data.get("username")
        else:
            username = request.data.get("email")
        password = request.data.get("password")
        # password = request.data.get("email")
        user = authenticate(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        if user:
            return Response({"token": token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(settings.LOGIN_URL)
#
# class UserTypeCreate(APIView):
#     """
#     Creates the user.
#     """
#
#     def post(self, request, format='json'):
#         serializer = UserTypeSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)