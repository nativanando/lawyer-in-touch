from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Customer, Lawyer, Contract

"""
This file provides the behavior of API methods. in the UserSerializer class we overrrided the method to create user to django pattern, using features such as
creating hash and validators.
the class below is an example of how modify a method and override a native django function.
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    These fields are handle by validators components
    """
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        """
        This function make a call in the django native method to create user.
        """
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    def recent_users(self):
        """
        This function is used to make a raw query and send the response to a specific view.
        It's an importante feature!! =)
        """
        recent_users = User.objects.raw('select * from auth_user')
        page = self.paginate_queryset(recent_users)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


    class Meta:
        model = User
        """
        These fields are going to available by API
        """
        fields = ('url', 'username', 'email', 'groups', 'password')

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class LawyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lawyer
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
