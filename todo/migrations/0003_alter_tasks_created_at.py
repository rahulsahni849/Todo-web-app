# Generated by Django 4.1.2 on 2022-10-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_todo_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
