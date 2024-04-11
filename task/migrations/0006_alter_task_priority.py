# Generated by Django 5.0.1 on 2024-04-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0005_alter_task_options_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[(1, "High"), (2, "Medium"), (3, "Low")],
                default=1,
                max_length=31,
            ),
        ),
    ]