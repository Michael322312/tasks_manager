from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("DONE",'Done'),
        ("TO_DO", "To do"),
        ("IN_PROGRESS", "In progress")
    ]
    
    PRIORITY_CHOISES = [
        ("1", "High"),
        ("2", "Medium"),
        ("3", "Low")
    ]

    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    due_to_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=31, choices=STATUS_CHOICES, default="TO_DO")
    priority = models.CharField(max_length=31, choices=PRIORITY_CHOISES, default="LOW")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        ordering = ['priority']