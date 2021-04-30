from django.http import HttpResponse
from rest_framework import serializers
# from django.contrib.auth.models import User, Group

from . import (models)


class OperationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Operation
        fields = '__all__'


class DevicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Devices
        fields = '__all__'


class DeveiceGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DeveiceGroup
        fields = '__all__'


class VMDSSerailizers(serializers.ModelSerializer):
    class Meta:
        model = models.VMDS
        fields = "__all__"

class RegionDimensionAndCoOrdinatesSSerailizers(serializers.ModelSerializer):
    class Meta:
        model = models.RegionDimensionAndCoOrdinates
        fields = "__all__"

class ScheduleSerailizers(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = "__all__"

class PlaylistSerailizers(serializers.ModelSerializer):
    createdDateFormat = serializers.DateTimeField(source='CreatedDate', format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = models.Playlist
        fields = "__all__"

class PublishManagementSerailizers(serializers.ModelSerializer):
    class Meta:
        model = models.PublishManagement
        fields = "__all__"

class TextMessageSerailizers(serializers.ModelSerializer):

    # RegionDimensionAndCoOrdinates = serializers.CharField(read_only=True)
    # Schedule = serializers.CharField(read_only=True)
    Message = serializers.SerializerMethodField(method_name='calculate_NoOfVmds', read_only=True)

    def calculate_NoOfVmds(self, value):
        try:
            if value.type == 'single':
                return "Single-Line Message"
            elif value.type == 'multi':
                return "Multi-Line Message"
            elif value.type == 'image':
                return "Image Message"
            elif value.type == 'video':
                return "Video Message"

        except Exception as e:
            return  "Nil"
    class Meta:
        model = models.TextMessage
        fields = "__all__"

    # def create(self, validated_data):
    #     try:
    #         RegionDimensionAndCoOrdinates = validated_data.pop('RegionDimensionAndCoOrdinates')
    #         Schedule = validated_data.pop('Schedule')
    #         RegionDimensionAndCoOrdinatesObj = models.RegionDimensionAndCoOrdinates.objects.get_or_create(
    #             **RegionDimensionAndCoOrdinates, user=validated_data.get('user'))
    #         ScheduleObj = models.Schedule.objects.get_or_create(**Schedule, user=validated_data.get('user'))
    #         obj = models.SingleLineTextMessage.objects.get_or_create(
    #             RegionDimensionAndCoOrdinates=RegionDimensionAndCoOrdinatesObj, ScheduleObj=ScheduleObj,
    #             **validated_data)
    #         return obj
    #     except Exception as e:
    #         print("Exception in SingleLineTextMessageSerailizers-Create : Error",str(e))
    #         return HttpResponse("Failed")

class VMDConfigSerailizers(serializers.ModelSerializer):
    class Meta:
        model = models.VMDConfig
        fields = "__all__"


class VMDGroupsSerailizers(serializers.ModelSerializer):
    createdDateFormat = serializers.DateTimeField(source='CreatedDate', format="%Y-%m-%d %H:%M:%S", read_only=True)
    NoOfVmds = serializers.SerializerMethodField(method_name='calculate_NoOfVmds', read_only=True)
    def calculate_NoOfVmds(self, value):
        try:
            return value.VMDS.all().count()
        except Exception as e:
            return 0
    class Meta:
        model = models.VMDGroups
        fields = "__all__"


class UsersSerailizers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        user = models.CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ' '),
            last_name=validated_data.get('last_name', ' ')
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

