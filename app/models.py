from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    role = models.CharField(max_length=500, blank=True)

class Operation(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Devices(models.Model):
    name = models.CharField(max_length=200)
    operation = models.ManyToManyField(Operation)

    def __str__(self):
        return self.name


class DeveiceGroup(models.Model):
    name = models.CharField(max_length=300)
    device = models.ManyToManyField(Devices)

    def __str__(self):
        return self.name


class VMDS(models.Model):
    VMDName = models.CharField(max_length=200)
    VMDLocation = models.CharField(max_length=200)
    VMDLatitude = models.CharField(max_length=200)
    VMDLongitude = models.CharField(max_length=200)
    VMDIPAddress = models.GenericIPAddressField(max_length=200, verbose_name="IP Address")
    VMDPort = models.IntegerField()
    VMDResolutionHeight =models.IntegerField()
    VMDResolutionwidth = models.IntegerField()
    VMDStatus = models.CharField(max_length=200)
    VMDBrightness = models.IntegerField()
    AssigneUser = models.CharField(max_length=200)


class VMDGroups(models.Model):
    GroupName = models.CharField(max_length=300)
    CreatedBy = models.CharField(max_length=300)
    CreatedDate = models.DateTimeField(auto_now=True)
    VMDS = models.ManyToManyField(VMDS)


class VMDConfig(models.Model):
    VMDS = models.ManyToManyField(VMDS)
    ON_OFF_Scheduling = models.BooleanField()
    VMD_Brightness = models.BooleanField()
    Resolution = models.BooleanField()
    wakeUptime = models.TimeField(null=True, blank=True)
    Sleeptime = models.TimeField(null=True, blank=True)
    Reboottime = models.TimeField(null=True, blank=True)
    Brightness = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)


class RegionDimensionAndCoOrdinates(models.Model):
    XCoOrdinates = models.IntegerField()
    YCoOrdinates = models.IntegerField()
    Width = models.IntegerField()
    Height = models.IntegerField()
    BorderLine = models.CharField(max_length=200)
    BackGroundColor = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Schedule(models.Model):
    StartDate = models.DateField()
    StartTime = models.TimeField()
    Duration = models.CharField(max_length=100)
    RepeatCount = models.IntegerField()
    type = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Playlist(models.Model):
    playlistname = models.CharField(max_length=200)
    XCoOrdinates = models.IntegerField()
    YCoOrdinates = models.IntegerField()
    Width = models.IntegerField()
    Height = models.IntegerField()
    BorderLine = models.CharField(max_length=200)
    BackGroundColor = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    singleLineMessage = models.TextField(null=True, blank=True)
    multilineMessage = models.TextField(null=True, blank=True)
    imageMessage = models.FileField(null=True, blank=True)
    videoMessage = models.FileField(null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class TextMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    RegionDimensionAndCoOrdinates = models.ForeignKey(RegionDimensionAndCoOrdinates, on_delete=models.CASCADE)
    Schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    type = models.CharField(max_length=200)
    text = models.TextField()


class PublishManagement(models.Model):
    vmd = models.ManyToManyField(VMDS, null=True, blank=True)
    vmdGroups = models.ManyToManyField(VMDGroups, null=True, blank=True)
    message = models.CharField(max_length=500)
    Schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
