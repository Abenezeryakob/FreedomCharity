# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20170425_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(blank=True, null=True, default=datetime.datetime(2017, 4, 25, 17, 31, 4, 217437)),
        ),
    ]
