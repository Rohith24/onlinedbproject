# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=25)),
                ('contact', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transform', models.IntegerField()),
                ('from_custom_base26', models.IntegerField()),
                ('get_pig_latin', models.IntegerField()),
                ('top_chars', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.EmailField(max_length=256)),
                ('dbnames', models.CharField(max_length=100)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrnd.Colleges')),
            ],
        ),
        migrations.AddField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrnd.Students'),
        ),
    ]
