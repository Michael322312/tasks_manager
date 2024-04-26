from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Task(models.Model):
    STATUS_CHOICES = [
        ("DONE", 'Done'),
        ("TO_DO", "To do"),
        ("IN_PROGRESS", "In progress")
    ]

    PRIORITY_CHOISES = [
        ("1", "High"),
        ("2", "Medium"),
        ("3", "Low")
    ]

    URL_TYPE = [
        ("WEBSITE", "Website"),
        ("ONLINE_MEETING", "Online meeting"),
        ("YT_VIDEO", "Youtube video")
    ]

    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    due_to_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=31,
        choices=STATUS_CHOICES,
        default="TO_DO"
    )
    priority = models.CharField(
        max_length=31,
        choices=PRIORITY_CHOISES,
        default="LOW"
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    task_for = models.ManyToManyField(User, blank=True)
    url_html = models.CharField(max_length=200, blank=True)

    url_type_choice = models.CharField(
        max_length=31,
        choices=URL_TYPE,
        default=None,
        blank=True
    )

    class Meta:
        ordering = ['priority', 'due_to_date']


class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    create_date = models.DateField(auto_now=True)
    file = models.FileField(blank=True, upload_to="comment_media", null=True)
    likes = models.ManyToManyField(User, related_name="liked_comments")

    class Meta:
        ordering = ['-create_date', "-id"]


    def get_comments(self):
        task = Task.objects.get(self.kwargs.get("pk"))
        return task.comments.all()

    def get_coment_age(self):
        today = date.today()
        created_date = self.create_date
        delta = today - created_date
        if delta.days == 0:
            return "Today"
        elif delta.days == 1:
            return "1 day ago"
        elif delta.days < 0:
            return f"How this user can write {delta.days} ago?"
        else:
            return f"{delta.days} days ago"


@receiver(pre_delete, sender=Comment)
def image_model_delete(sender, instance, **kwargs):
    if instance.file.name:
        instance.file.delete(False)
