from rest_framework import serializers

from classroom.models.users import Users


class LoginSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()

    def create(self, validated_data):
        validated_data['password'] = Users.objects.make_random_password()
        return Users.objects.create(**validated_data)

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


class RegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.RegexField(r'^\+?1?\d{9,15}$')

    class Meta:
        model = Users
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
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
