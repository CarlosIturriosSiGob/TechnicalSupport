# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 04:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanager', '0003_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Poll',
        ),
    ]
