# Generated by Django 2.2 on 2020-05-09 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pacific', '0005_event_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
