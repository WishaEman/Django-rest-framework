from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from http import HTTPStatus


class LoginView(APIView):
    """
        This view provides a post request to login a user.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({
                'status': HTTPStatus.OK,
                'token': token.key,
            })
        return Response({
            'status': HTTPStatus.NOT_FOUND,
            'message': 'Invalid Credentials'
        })


class SignupView(CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'status': 204,
            'message': 'Successfully Logged out User'
        })

