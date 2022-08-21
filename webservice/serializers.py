from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['Phone', 'Context', 'Service']




