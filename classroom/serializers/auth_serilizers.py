from django.contrib.auth import authenticate
from rest_framework import serializers

from classroom.models.users import User


class LoginSerializer(serializers.Serializer):
    def create(self, validated_data):
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        return {
            'email': user.email,
            'token': user.token
        }

    def update(self, instance, validated_data):
        pass

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        return {
            'email': user.email,
            'token': user.token
        }

    class Meta:
        fields = ('email', 'password')


class RegistrationSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            raise serializers.ValidationError(
                'A user with this email and password already exists.'
            )
        return {
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name
        }

    class Meta:
        model = User
        fields = '__all__'
