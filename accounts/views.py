from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics, status

class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = RefreshToken.for_user(user)
        tokens = {
            'refresh_token': str(token),
            'access_token': str(token.access_token)
        }
        return Response(tokens, status=status.HTTP_200_OK)