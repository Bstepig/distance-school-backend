# Generated by Django 3.0.5 on 2020-04-28 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_answerattachment_attachment_taskanswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='task',
        ),
        migrations.DeleteModel(
            name='AnswerAttachment',
        ),
    ]
