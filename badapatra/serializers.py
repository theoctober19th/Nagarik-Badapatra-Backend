from rest_framework import serializers
from badapatra import models

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    class Meta:
        model = models.Floor
        fields = (
            'id',
            'floor',
            'room',
        )

class BuildingSerializer(serializers.ModelSerializer):
    floor =FloorSerializer()
    class Meta:
        model  = models.Building
        fields = (
            'id',
            'building',
            'floor'
        )
