# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-08-25 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200825_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=512, verbose_name='博客内容'),
        ),
    ]