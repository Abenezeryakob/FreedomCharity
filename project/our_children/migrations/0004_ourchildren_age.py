# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_children', '0003_auto_20170423_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourchildren',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
