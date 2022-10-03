from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers,validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','phone','password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = ['username','email','phone','password']

        extra_kwargs = {
            "password": {"write_only":True},
            "email":{
                "required":True,
                "allow_blank":False,
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that email already exists"
                    )
                ]
            },
            "phone": {"required":True},

        }


    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data('password')
        email = validated_data('email')
        phone = validated_data('phone')

        user = User.objects.create(
            username=username,
            password = password,
            email=email,
            phone = phone,
        )

        return user