from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.blog.models import Category, Blog, Comment


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['title',
                    'slug',
                    'body',
                    'posted',
                    'category',
                    'comments']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'blog',
            'text'
        ]

