from rest_framework import serializers

from classroom.models.buildings import Buildings


class BuildingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buildings
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('is_deleted', 'status', None)
        return super().create(validated_data)
