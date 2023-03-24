from rest_framework import serializers

from classroom.models import Department
from classroom.models.users import Users


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    token = serializers.CharField()
    token_type = serializers.CharField()
    expires_in = serializers.IntegerField()
    refresh_token = serializers.CharField()
    scope = serializers.CharField()
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())


class RegistrationSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(r'^\+?1?\d{9,15}$')
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    number_of_students = serializers.IntegerField(required=False)
    date_of_birth = serializers.DateField()
    first_name = serializers.CharField()
    last_name = serializers.CharField(required=False)
    gender = serializers.ChoiceField(choices=('M', 'F', 'X'))
    token = serializers.CharField(required=False)
    level = serializers.ChoiceField(choices=(200, 300, 400, 500, 600))
    is_assistant = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Remove the 'password' field from the output
        data.pop('password', None)
        return data

    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class RegistrationResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    full_name = serializers.CharField()


class LogoutSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    token = serializers.CharField()
    message = serializers.CharField()
