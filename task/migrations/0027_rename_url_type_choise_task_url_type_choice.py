# Generated by Django 5.0.1 on 2024-04-26 10:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0026_alter_comment_unique_together_task_url_html_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="url_type_choise",
            new_name="url_type_choice",
        ),
    ]