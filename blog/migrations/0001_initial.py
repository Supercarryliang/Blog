# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-08-24 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='博客内容')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('评论内容', models.CharField(max_length=256)),
                ('c_blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='用户名字')),
                ('password', models.CharField(max_length=32, verbose_name='用户密码')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='c_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]
