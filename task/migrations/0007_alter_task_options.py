# Generated by Django 5.0.1 on 2024-04-06 10:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0006_alter_task_priority"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-priority"]},
        ),
    ]