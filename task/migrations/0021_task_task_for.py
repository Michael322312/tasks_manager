# Generated by Django 5.0.1 on 2024-04-17 17:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0020_rename_author_comment_creator"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="task_for",
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]