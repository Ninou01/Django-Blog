# Generated by Django 3.0.1 on 2020-06-14 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200613_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 14, 18, 54, 43, 297172)),
        ),
    ]
