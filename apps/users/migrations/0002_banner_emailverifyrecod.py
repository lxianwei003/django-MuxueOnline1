# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-12 12:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerifyRecod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='\u9a8c\u8bc1\u7801')),
                ('email', models.EmailField(max_length=30, verbose_name='\u90ae\u7bb1')),
                ('send_type', models.CharField(choices=[('register', '\u767b\u9646'), ('forget', '\u627e\u5bc6\u7801')], max_length=20)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u90ae\u7bb1\u9a8c\u8bc1',
                'verbose_name_plural': '\u90ae\u7bb1\u9a8c\u8bc1',
            },
        ),
    ]