from django.urls import path, include
from .views import TaskViewSet, UserTasks, CompleteTasks, LogViewSet, CommentViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'logs', LogViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('myTasks', UserTasks.as_view()),
    path('completeTasks', CompleteTasks.as_view()),
]
