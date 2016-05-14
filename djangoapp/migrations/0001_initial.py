# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('command', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_type', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_note', models.CharField(max_length=50)),
                ('note_date', models.DateField()),
                ('note_time', models.TimeField()),
                ('user', models.ManyToManyField(to='djangoapp.CustomUser')),
            ],
        ),
        migrations.AddField(
            model_name='commandlog',
            name='user',
            field=models.ManyToManyField(to='djangoapp.CustomUser'),
        ),
    ]
