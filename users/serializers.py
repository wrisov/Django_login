from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate,login
from rest_framework import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer) :
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username= data.get("username","")
        password= data.get("password","")

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"] = user
        else:
            raise exceptions.ValidationError()
            
        return data


class SignupSerializer(serializers.Serializer) :
    username=serializers.CharField()
    password=serializers.CharField()
    role_id=serializers.IntegerField()
    