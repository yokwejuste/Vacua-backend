from rest_framework import serializers

from classroom.models.users import Users


class CCRegistrationSerializer(serializers.ModelSerializer):
    school = serializers.CharField(required=False)
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


class CCRegistrationResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    full_name = serializers.CharField()


class CCUpdateUserSerializer(serializers.ModelSerializer):
    school = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def update(self, instance, validated_data):
        instance.save()
        return instance


class CCUpdateUserSerializerResponse(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    full_name = serializers.CharField()
