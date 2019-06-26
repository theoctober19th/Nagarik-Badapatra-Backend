from django.shortcuts import render
from badapatra.serializers import BuildingSerializer, RoomSerializer, FloorSerializer
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from badapatra.models import Building, Room, Floor


class BuildingViewset(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


