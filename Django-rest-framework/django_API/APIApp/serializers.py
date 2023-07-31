from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book, Author


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        """
        to_representation, to customize the serialized output
        """
        representation = super().to_representation(instance)

        representation['full_title'] = f"{instance.title} And Genre is ({instance.genre})"
        representation['author_name'] = instance.author.name

        return representation


class AuthorSerializer(serializers.ModelSerializer):
    """
    In the AuthorSerializer, the BookSerializer is as a nested serializer using the books field.
    many=True because an author can have multiple books.
    """
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'country', 'books']

    def create(self, validated_data):
        books_data = validated_data
        author_obj = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author_obj, **book_data)
        return author_obj

    def update(self, instance, validated_data):
        print(validated_data)
        # print(instance)
        books_data = validated_data.pop('books')
        # prev_books = (instance.books).all()
        # prev_books = list(prev_books)
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()

        # for book_data in books_data:
        #     instance.book.title = book_data.get('title', book_data.title)
        #     instance.book.genre = book_data.get('genre', book_data.genre)
        #     instance.book.save()
        return instance
