from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #admin
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    priority = models.IntegerField()
    deadline = models.DateField()
    title = models.CharField(max_length=100, default="未命名任務")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

