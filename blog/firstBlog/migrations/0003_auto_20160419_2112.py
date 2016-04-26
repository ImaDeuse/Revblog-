# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstBlog', '0002_auto_20160419_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_title',
            field=models.CharField(max_length=180),
        ),
    ]
