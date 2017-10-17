# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-14 09:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0007_auto_20171014_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mod_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='monthly_order1',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 60', validators=[django.core.validators.MaxValueValidator(60)], verbose_name='Marks and Maxwell'),
        ),
        migrations.AlterField(
            model_name='product',
            name='monthly_order2',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 75', validators=[django.core.validators.MaxValueValidator(75)], verbose_name='Chopra and Company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='monthly_order3',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 100', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Daggit Enterprises'),
        ),
        migrations.AlterField(
            model_name='product2',
            name='mod_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product2',
            name='monthly_order1',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 60', validators=[django.core.validators.MaxValueValidator(60)], verbose_name='Marks and Maxwell'),
        ),
        migrations.AlterField(
            model_name='product2',
            name='monthly_order2',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 75', validators=[django.core.validators.MaxValueValidator(75)], verbose_name='Chopra and Company'),
        ),
        migrations.AlterField(
            model_name='product2',
            name='monthly_order3',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 100', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Daggit Enterprises'),
        ),
        migrations.AlterField(
            model_name='product3',
            name='mod_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product3',
            name='monthly_order1',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 60', validators=[django.core.validators.MaxValueValidator(60)], verbose_name='Marks and Maxwell'),
        ),
        migrations.AlterField(
            model_name='product3',
            name='monthly_order2',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 75', validators=[django.core.validators.MaxValueValidator(75)], verbose_name='Chopra and Company'),
        ),
        migrations.AlterField(
            model_name='product3',
            name='monthly_order3',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 100', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Daggit Enterprises'),
        ),
        migrations.AlterField(
            model_name='product4',
            name='mod_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product4',
            name='monthly_order1',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 60', validators=[django.core.validators.MaxValueValidator(60)], verbose_name='Marks and Maxwell'),
        ),
        migrations.AlterField(
            model_name='product4',
            name='monthly_order2',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 75', validators=[django.core.validators.MaxValueValidator(75)], verbose_name='Chopra and Company'),
        ),
        migrations.AlterField(
            model_name='product4',
            name='monthly_order3',
            field=models.PositiveIntegerField(default=0, help_text='Max Value is 100', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Daggit Enterprises'),
        ),
    ]