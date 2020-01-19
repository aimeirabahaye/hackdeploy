from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import PosterSerializer, WorkerSerializer, MessageSerializer, TaskSerializer
from .models import Poster, Worker, Message, Task

class PosterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows LUTs to be viewed or edited.
    """
    queryset = Poster.objects.all().order_by('id')
    serializer_class = PosterSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows LUTs to be viewed or edited.
    """
    queryset = Worker.objects.all().order_by('id')
    serializer_class = WorkerSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows LUTs to be viewed or edited.
    """
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows LUTs to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
