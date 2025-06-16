from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'priority', 'user', 'created_at']
    list_filter = ['status', 'priority', 'is_completed', 'created_at']
    search_fields = ['name', 'status', 'title']
    ordering = ['-created_at']


