from rest_framework import routers
from . import (viewset)


router = routers.SimpleRouter()
router.register('api/Deveice', viewset.DeveiceViewSet)
router.register('api/Users', viewset.UsersViewSet)
router.register('api/VMDS', viewset.VMDSViewSet)
router.register('api/VMDGroups', viewset.VMDGroupsViewSet)
router.register('api/VMDConfig', viewset.VMDConfigViewSet)
router.register('api/TextMessage', viewset.TextMessageViewSet)
router.register('api/RegionDimensionAndCoOrdinates', viewset.RegionDimensionAndCoOrdinatesViewSet)
router.register('api/Schedule', viewset.ScheduleViewSet)
router.register('api/PublishManagement', viewset.PublishManagementViewSet)