from django.urls import path, include
from .views import *

app_name = 'authentication_api'

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('logout/', LogoutView.as_view()),
]