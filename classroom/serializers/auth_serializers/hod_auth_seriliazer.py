from rest_framework import serializers

from classroom.models.users import Users


class HodRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.RegexField(r'^\+?1?\d{9,15}$')
    school = serializers.CharField(required=None)

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


class HodRegistrationResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    full_name = serializers.CharField()


class HodUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def update(self, instance, validated_data):
        instance.save()
        return instance


class HodUpdateUserSerializerResponse(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    full_name = serializers.CharField()
