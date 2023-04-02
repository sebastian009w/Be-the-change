"""DJANGO"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """Task."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)