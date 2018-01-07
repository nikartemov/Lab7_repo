# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='team',
            name='games',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='win',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
