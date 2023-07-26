from django.contrib.auth.models import User, Group
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(ListCreateAPIView):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(ListCreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
