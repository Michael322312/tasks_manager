# Generated by Django 5.0.1 on 2024-04-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0027_rename_url_type_choise_task_url_type_choice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="url_html",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
