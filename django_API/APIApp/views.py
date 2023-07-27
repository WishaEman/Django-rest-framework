from django.contrib.auth.models import User, Group
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from .serializers import UserSerializer, GroupSerializer, BookSerializer, AuthorSerializer
from .models import Book, Author

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserViewSet(ListCreateAPIView):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BookViewSet(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookUpdateView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book created successfully."})
        else:
            return Response(serializer.errors)


class BookChangeView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."})

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."})

        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book updated successfully."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
