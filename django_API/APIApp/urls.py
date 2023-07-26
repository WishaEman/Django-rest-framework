from django.urls import path
from .views import UserViewSet, GroupViewSet

app_name = 'APIApp'


urlpatterns = [
    path('user/', UserViewSet.as_view(), name='user'),
    path('group/', GroupViewSet.as_view(), name='group'),
]

