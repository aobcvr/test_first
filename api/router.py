from .views import DealViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('deals', DealViewSet, basename='deals')
