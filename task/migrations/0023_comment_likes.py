# Generated by Django 5.0.1 on 2024-04-24 17:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0022_alter_comment_options_alter_task_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.ManyToManyField(
                related_name="comments_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
