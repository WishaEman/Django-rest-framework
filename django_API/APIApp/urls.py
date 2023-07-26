from django.urls import path
from .views import UserViewSet, GroupViewSet, BookViewSet, AuthorViewSet, BookCreateView, BookUpdateView, BookChangeView


app_name = 'APIApp'


urlpatterns = [
    path('user/', UserViewSet.as_view(), name='user'),
    path('group/', GroupViewSet.as_view(), name='group'),
    path('book/', BookViewSet.as_view(), name='book'),
    path('author/', AuthorViewSet.as_view(), name='author'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/update/<int:pk>/', BookChangeView.as_view(), name='books_change'),
]

