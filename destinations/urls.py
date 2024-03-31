from django.urls import path, include
from destinations import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api', views.DestinationAPIView, basename='destinations')


urlpatterns = [
    path('', include(router.urls))
]
