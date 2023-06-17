from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, UserRequestViewSet

router = DefaultRouter()
router.register('elevators', ElevatorViewSet)
router.register('requests', UserRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]