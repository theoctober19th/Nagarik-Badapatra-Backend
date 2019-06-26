from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    room_no = models.IntegerField()
    pass

class Floor(models.Model):
    pass


class Building(models.Model):
    pass
