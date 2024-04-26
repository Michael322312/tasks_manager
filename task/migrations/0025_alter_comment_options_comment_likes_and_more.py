# Generated by Django 5.0.1 on 2024-04-26 05:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0024_alter_comment_options_remove_comment_likes_like"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-create_date", "-id"]},
        ),
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.ManyToManyField(
                related_name="liked_comments", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name="comment",
            unique_together={("id",)},
        ),
        migrations.DeleteModel(
            name="Like",
        ),
    ]
