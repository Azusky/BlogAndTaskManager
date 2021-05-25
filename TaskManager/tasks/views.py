from django.shortcuts import render
from django.contrib.auth.models import User
from tasks.serializers import TaskSerializer, CommentSerializer, LogSerializer
from rest_framework import generics, viewsets, permissions, status
from tasks.models import Task, Comment, Log
from tasks.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from rest_framework.response import Response

from django.core.mail import EmailMessage
from users.serializers import UserSerializer

from rest_framework.decorators import action
from datetime import datetime, timezone


def send_email(title, description, to):
    email = EmailMessage(
        title,
        description,
        to=[to]
    )

    email.send()


class UserTasks(generics.ListAPIView):

    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(assign=user).all()


class CompleteTasks(generics.ListAPIView):
    queryset = Task.objects.filter(status="complete").all()
    serializer_class = TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save(owner=self.request.user)
        send_email(title=task.title, description=task.description,
                   to=task.assign.email)

    def perform_update(self, serializer):

        task = serializer.save(owner=self.request.user)
        if task.status == 'complete':
            send_email(title=task.title, description=task.status,
                       to=task.assign.email)

    @action(detail=True, methods=['get'])
    def start_log(self, request, pk):
        task = self.get_object()

        try:
            log = Log.objects.filter(task_id=pk).latest("start_data")
        except  Log.DoesNotExist:

            log = Log(duration=0, task_id=task.id)
            log.save()
            return Response({'status': 'Start Task'})
        else:

            return Response({'status': 'Task has been started'})


    @action(detail=True, methods=['get'])
    def end_log(self, request, pk):
        task = self.get_object()
        log = Log.objects.filter(task_id=pk).latest("start_data")
        datetime_end = datetime.now(timezone.utc)

        minutes_diff = (datetime_end - log.start_data).total_seconds() / 60.0

        if log.duration == 0:

            log.duration = minutes_diff
            log.save()
            return Response({'status': 'Stop Task'})
        else:
            return Response({'status': 'Task has been stopped'})



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter()
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)
        send_email(title=comment.task.title, description=comment.body,
                   to=comment.task.assign.email)


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.filter()
    permission_classes = (AllowAny,)
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
