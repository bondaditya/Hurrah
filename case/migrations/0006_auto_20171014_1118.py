# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-14 05:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0005_auto_20171012_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='gesture',
            new_name='gestures',
        ),
    ]
