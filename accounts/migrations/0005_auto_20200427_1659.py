# Generated by Django 3.0.5 on 2020-04-27 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200427_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_director',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='director',
            name='school',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.School'),
        ),
    ]