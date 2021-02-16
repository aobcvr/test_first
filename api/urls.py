from rest_framework import routers

from .views import DealViewSet

router = routers.DefaultRouter()

router.register('deals', DealViewSet, basename='deals')

urlpatterns = router.urls
