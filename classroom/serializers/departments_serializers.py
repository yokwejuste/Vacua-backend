from rest_framework import serializers

from classroom.models.departments import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('is_deleted', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('is_deleted', None)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['school'] = instance.school.name
        return data
