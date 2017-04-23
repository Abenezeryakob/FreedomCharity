# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('our_children', '0002_auto_20170423_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourchildren',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
