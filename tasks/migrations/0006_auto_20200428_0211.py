# Generated by Django 3.0.5 on 2020-04-27 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='body',
        ),
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='task',
            name='lesson',
        ),
    ]
