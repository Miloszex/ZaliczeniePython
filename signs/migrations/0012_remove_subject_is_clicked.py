# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-10 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0011_subject_is_clicked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='is_clicked',
        ),
    ]
