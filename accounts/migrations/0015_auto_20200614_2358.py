# Generated by Django 3.0.1 on 2020-06-14 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200614_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 14, 23, 58, 36, 789551)),
        ),
    ]