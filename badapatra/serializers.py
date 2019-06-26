from rest_framework import serializers
from badapatra import models

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Building
        fields = '__all__'
