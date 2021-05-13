from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response

from . import (models, serializers)
# from django.contrib.auth.models import User, Group


class OperationViewSet(viewsets.ModelViewSet):
    queryset = models.Operation.objects.all()
    serializer_class = serializers.OperationSerializers


class DeveiceGroupViewSet(viewsets.ModelViewSet):
    queryset = models.DeveiceGroup.objects.all()
    serializer_class = serializers.DeveiceGroupSerializers


class DeveiceViewSet(viewsets.ModelViewSet):
    queryset = models.Devices.objects.all()
    serializer_class = serializers.DevicesSerializers


class VMDSViewSet(viewsets.ModelViewSet):
    queryset = models.VMDS.objects.all()
    serializer_class = serializers.VMDSSerailizers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    filterset_fields = ['id']


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = models.Reports.objects.all()
    serializer_class = serializers.ReportsSerailizers


class VMDConfigViewSet(viewsets.ModelViewSet):
    queryset = models.VMDConfig.objects.all()
    serializer_class = serializers.VMDConfigSerailizers
#
class PublishManagementViewSet(viewsets.ModelViewSet):
    queryset = models.PublishManagement.objects.all()
    serializer_class = serializers.PublishManagementSerailizers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','type', 'user']
    filterset_fields = ['id','type', 'user']
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializers.PlaylistSerailizers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'playlistname', 'XCoOrdinates', 'YCoOrdinates', 'Width', 'Height', 'BorderLine', 'BackGroundColor', 'type', 'singleLineMessage', 'multilineMessage', 'CreatedDate', 'user']
    filterset_fields = ['id', 'playlistname', 'XCoOrdinates', 'YCoOrdinates', 'Width', 'Height', 'BorderLine', 'BackGroundColor', 'type', 'singleLineMessage', 'multilineMessage', 'CreatedDate', 'user']
    search_fields  = [ 'playlistname',  'singleLineMessage', 'multilineMessage']

class TextMessageViewSet(viewsets.ModelViewSet):
    queryset = models.TextMessage.objects.all()
    serializer_class = serializers.TextMessageSerailizers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'user', 'RegionDimensionAndCoOrdinates', 'Schedule','type', 'text']

    filterset_fields = ['id', 'user', 'RegionDimensionAndCoOrdinates', 'Schedule','type', 'text']


class RegionDimensionAndCoOrdinatesViewSet(viewsets.ModelViewSet):
    queryset = models.RegionDimensionAndCoOrdinates.objects.all()
    serializer_class = serializers.RegionDimensionAndCoOrdinatesSSerailizers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = [field.name for field in models.RegionDimensionAndCoOrdinates._meta.fields]
    filterset_fields = [field.name for field in models.RegionDimensionAndCoOrdinates._meta.fields]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerailizers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = [field.name for field in models.Schedule._meta.fields]
    filterset_fields = [field.name for field in models.Schedule._meta.fields]


class VMDGroupsViewSet(viewsets.ModelViewSet):
    queryset = models.VMDGroups.objects.all()
    serializer_class = serializers.VMDGroupsSerailizers


class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UsersSerailizers

    @action(detail=False, methods=['GET'])
    def currentuser(self, request):
        return Response(serializers.UsersSerailizers(request.user).data)