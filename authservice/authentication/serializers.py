# Author: bbrighttaer
# Project: authservice
# Date: 10/23/2020
# Time: 5:11 AM
# File: serializers.py

from __future__ import absolute_import, division, print_function, unicode_literals

from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('The username should be alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.DictField(child=serializers.CharField(max_length=555, min_length=3),
                                   read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid login credentials, try again')
        elif not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        elif not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {'email': user.email, 'username': user.username, 'tokens': user.tokens()}


class LogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555, min_length=3, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'token']
