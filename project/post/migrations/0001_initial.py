# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30, blank=True, null=True)),
                ('post_note', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateTimeField(blank=True, null=True, default=datetime.datetime(2017, 4, 25, 12, 36, 3, 36530))),
                ('slug', models.SlugField(max_length=100, blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
