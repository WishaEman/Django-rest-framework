from django.urls import path
from .views import *

app_name = 'APIApp'


urlpatterns = [
    path('user/', UserViewSet.as_view(), name='user'),
    path('group/', GroupViewSet.as_view(), name='group'),
    path('book/', BookViewSet.as_view(), name='book'),
    path('author/', AuthorViewSet.as_view(), name='author'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
]

