# Generated by Django 5.0.1 on 2024-04-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0016_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("HIGH", "High"), ("MEDIUM", "Medium"), ("LOW", "Low")],
                default="LOW",
                max_length=31,
            ),
        ),
    ]