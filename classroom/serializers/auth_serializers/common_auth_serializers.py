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


class ChangePasswordSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        if validated_data['new_password'] != validated_data['repeat_password']:
            raise serializers.ValidationError('New password and repeat new password must be same')

    old_password = serializers.CharField()
    new_password = serializers.CharField()
    repeat_password = serializers.CharField()


class LogoutSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    token = serializers.CharField()
    message = serializers.CharField()
