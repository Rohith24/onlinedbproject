# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrnd', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colleges',
            old_name='college',
            new_name='Acronym',
        ),
    ]
