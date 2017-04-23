# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('our_children', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurChildenProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('our_children.ourchildren',),
        ),
        migrations.AddField(
            model_name='ourchildren',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ourchildren',
            name='first_name',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ourchildren',
            name='last_name',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
