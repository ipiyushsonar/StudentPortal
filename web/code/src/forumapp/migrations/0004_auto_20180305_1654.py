# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0003_comment_author_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]