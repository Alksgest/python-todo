from django.contrib.auth.models import User
from rest_framework import serializers

from .models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TodoModel
        fields = ('id', 'date', 'content', 'owner')

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=TodoModel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'todos')