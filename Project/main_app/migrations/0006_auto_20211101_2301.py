# Generated by Django 3.2.8 on 2021-11-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20211024_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastName',
        ),
        migrations.AddField(
            model_name='profile',
            name='fullName',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
