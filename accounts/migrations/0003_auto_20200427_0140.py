# Generated by Django 3.0.5 on 2020-04-26 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_director_grade_parent_school_student_subject_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='student',
        ),
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('D', 'Director'), ('S', 'Student'), ('T', 'Teacher'), ('P', 'Parent'), ('A', 'Admin')], default='S', max_length=1),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]