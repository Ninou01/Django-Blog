# Generated by Django 3.0.1 on 2020-06-29 12:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200629_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 12, 45, 20, 756363, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 13, 45, 20, 755367)),
        ),
    ]