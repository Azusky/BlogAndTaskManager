from rest_framework import viewsets
from rest_framework import status

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter()
    permission_classes = (AllowAny,)
    serializer_class = BlogSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter()
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer
