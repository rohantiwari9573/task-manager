from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'created_at', 'updated_at']

    # 🔥 VALIDATION
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        return value


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()