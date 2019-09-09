from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token

class UserList(APIView):
    def get(self,request):
        users=User.objects.all
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)


class LoginView(APIViews):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        django_login(request,user)
        token, created = Token.objects.get_or_create(user=user)
        return Response ({"token": token.key},status=200)
