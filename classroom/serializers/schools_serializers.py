from rest_framework import serializers

from classroom.models import Schools


class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('is_deleted', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('is_deleted', None)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['university'] = instance.university.name
        return data
