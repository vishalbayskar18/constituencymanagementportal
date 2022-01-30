# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('against', models.CharField(max_length=50)),
                ('aginst_id', models.IntegerField()),
                ('detail', models.CharField(max_length=250)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
