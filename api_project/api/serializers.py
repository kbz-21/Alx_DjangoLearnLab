from rest_framework import serializers
from .models import Book   # make sure Book model is imported correctly

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # includes all fields in the Book model
