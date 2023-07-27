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

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

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
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'country', 'books']

    def create(self, validated_data):
        return Author.objects.create(**validated_data)