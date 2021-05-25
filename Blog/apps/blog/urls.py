from django.urls import path, include
from apps.blog.views import CategoryViewSet, CommentViewSet, BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'blog', BlogViewSet, basename='blog')

urlpatterns = [path('', include(router.urls))]
