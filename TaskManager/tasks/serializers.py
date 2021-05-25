
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from tasks.models import Task, Comment, Log




class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Task
        fields = ['id','title', 'description','status', 'owner','comments','assign']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'task']



class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'start_data', 'duration', 'task']
