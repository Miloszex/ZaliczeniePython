# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-06 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0007_remove_subject_is_taken_by_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='space',
            field=models.IntegerField(default=0),
        ),
    ]
