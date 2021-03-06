# Generated by Django 3.0.1 on 2020-06-06 11:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 6, 6, 12, 47, 18, 12424))),
                ('slug', models.SlugField(blank=True)),
                ('img', models.ImageField(default='userimg/avatar.png', upload_to='userimg/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
