# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('command', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_note', models.CharField(max_length=50)),
                ('note_date', models.DateField()),
                ('note_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
                ('user_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ManyToManyField(to='djangoapp.User'),
        ),
        migrations.AddField(
            model_name='commandlog',
            name='user',
            field=models.ManyToManyField(to='djangoapp.User'),
        ),
    ]
