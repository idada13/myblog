# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-17 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=999),
        ),
    ]
