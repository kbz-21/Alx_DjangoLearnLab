from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like




User = get_user_model()

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = UserSimpleSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  # nested read-only
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comments_count']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at', 'comments', 'comments_count']



# posts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'profile_picture']

class PostSerializer(serializers.ModelSerializer):
    author = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']


User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    liked_by_me = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'likes_count', 'liked_by_me']

    def get_liked_by_me(self, obj):
        user = self.context.get('request').user
        if not user or user.is_anonymous:
            return False
        return obj.likes.filter(user=user).exists()
