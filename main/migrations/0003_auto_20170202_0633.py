# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-02 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170125_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('tag_desc', models.CharField(default='', max_length=500)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='opinion',
            name='foragainst',
            field=models.IntegerField(default=0),
        ),
    ]