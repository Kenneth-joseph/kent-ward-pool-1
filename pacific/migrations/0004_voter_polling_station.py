# Generated by Django 2.2 on 2020-05-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacific', '0003_remove_event_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='polling_station',
            field=models.CharField(default='gwasi', max_length=30),
        ),
    ]