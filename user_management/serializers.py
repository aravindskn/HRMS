from rest_auth.serializers import UserDetailsSerializer
from .models import User
from rest_auth.models import TokenModel
from rest_framework import serializers
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserDetailsSerializer(UserDetailsSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'employee', 'groups']
        read_only_fields = ('pk', 'username', 'employee', 'groups')


class TokenSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    class Meta:
        model = TokenModel
        fields = ['key', 'user']
