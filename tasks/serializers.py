from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    remaining_days = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'name', 'status', 'priority', 'deadline', 'remaining_days', 'user']
        read_only_fields = ['id', 'remaining_days', 'user']

    def get_remaining_days(self, obj):
        return (obj.deadline - date.today()).days

    def validate_priority(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('優先度須於 1~5 之間')
        return value

    def validate(self, data):
        if data.get('status') == '已完成' and data.get('priority') == 1:
            raise serializers.ValidationError('已完成的任務不該是最高優先度')
        return data
