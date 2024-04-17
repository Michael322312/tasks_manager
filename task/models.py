from django.db import models
from django.contrib.auth.models import User
from datetime import date


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

    task_for = models.ManyToManyField(User)

    class Meta:
        ordering = ['priority']


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    create_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-create_date']

       
    def get_coment_age(self):
        today = date.today()
        created_date = self.create_date
        delta = today - created_date
        if delta.days == 0:
            return "Today"
        else:
            return f"{delta.days} days ago"
    
