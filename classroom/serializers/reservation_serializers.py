from rest_framework import serializers

from classroom.models import Reservations


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'

    def create(self, validated_data):
        return Reservations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance
