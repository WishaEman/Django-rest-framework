from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

app_name = 'APIApp'

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('user', UserViewSet.as_view(), name='user'),
    path('group', GroupViewSet.as_view(), name='group'),
]

