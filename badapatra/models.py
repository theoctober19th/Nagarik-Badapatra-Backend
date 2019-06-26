from django.db import models

# class Documents(models.Model):
#     name = models.TextField(max_length=1500)
#     count = models.IntegerField()
#
# class Service(models.Model):
#     name = models.CharField(max_length=255)
#     time = models.IntegerField()
#     expense = models.IntegerField()
#     responsible_person = models.CharField(max_length=255)
#     complain_

class Room(models.Model):
    name = models.CharField(max_length=50)
    room_no = models.IntegerField()
    activity = models.TextField(max_length=255)
    time = models.TimeField()
    pass

class Floor(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    floor = models.IntegerField()

    pass


class Building(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    building = models.IntegerField()
    pass
