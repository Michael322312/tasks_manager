# Generated by Django 5.0.1 on 2024-04-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0025_alter_comment_options_comment_likes_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="comment",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="task",
            name="url_html",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="task",
            name="url_type_choise",
            field=models.CharField(
                choices=[
                    ("WEBSITE", "Website"),
                    ("ONLINE_MEETING", "Online meeting"),
                    ("YT_VIDEO", "Youtube video"),
                ],
                default="WEBSITE",
                max_length=31,
            ),
        ),
    ]