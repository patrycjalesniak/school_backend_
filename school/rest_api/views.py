from django.shortcuts import render
from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .permisions import IsExamOwnerOrReadOnly, IsOwnerReadOnly
from rest_framework import permissions


class ExamView(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly)


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsExamOwnerOrReadOnly)