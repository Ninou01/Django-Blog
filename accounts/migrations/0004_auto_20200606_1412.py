# Generated by Django 3.0.1 on 2020-06-06 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200606_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 14, 12, 27, 543959)),
        ),
    ]
