from rest_framework import serializers
from .models import Task


# =========================
# TASK SERIALIZER
# =========================
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# =========================
# REGISTER SERIALIZER (NEW)
# =========================
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)