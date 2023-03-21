from rest_framework import serializers

from classroom.models.halls import Halls


class HallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halls
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }

    def create(self, validated_data):
        validated_data.pop('is_deleted', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('is_deleted', None)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['building'] = instance.building.name
        data['school'] = instance.school.name
        return data
