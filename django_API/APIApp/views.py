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


# class AuthorUpdateView(RetrieveUpdateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class AuthorCreateView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Author created successfully."})
        else:
            return Response(serializer.errors)


class AuthorUpdateView(APIView):
    def get_author(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return None

    def get(self, request, pk):
        author = self.get_author(pk)
        if not author:
            return Response({"error": "Author not found."})
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_author(pk)
        if not author:
            return Response({"error": "Author not found."})

        serializer = AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Author updated successfully."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

