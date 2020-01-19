from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Poster, Worker, Message, Task

class PosterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    profile_image = serializers.ImageField()
    description = serializers.CharField(max_length=250)
 
    def create(self, validated_data):
        """
        Create and return a new MEAL instance, given the validated data.
        """
        return  Poster.objects.create(**validated_data)


class WorkerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    profile_image = serializers.ImageField()
    description = serializers.CharField(max_length=250)
    rating = serializers.IntegerField()
    class Meta:
        ordering = ('last_name',)

    def create(self, validated_data):
        """
        Create and return a new MEAL instance, given the validated data.
        """
        return  Worker.objects.create(**validated_data)

class MessageSerializer(serializers.Serializer):
    worker_id = serializers.IntegerField()
    task_id = serializers.IntegerField()
    
    message_content = serializers.CharField(max_length=250)

    def create(self, validated_data):
        """
        Create and return a new MEAL instance, given the validated data.
        """
        return  Message.objects.create(**validated_data)

class TaskSerializer(serializers.Serializer):
    taskName = serializers.CharField(max_length=45)
    poster_id = serializers.IntegerField(default=0)

    category = serializers.ChoiceField(choices=Task.CATEGORIES)
    description = serializers.CharField(max_length=500)

    dueDate = serializers.DateField()
    latitude = serializers.DecimalField(decimal_places=6,max_digits=10)
    longtitude =  serializers.DecimalField(decimal_places=6,max_digits=10)
    status = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new MEAL instance, given the validated data.
        """
        return Task.objects.create(**validated_data)