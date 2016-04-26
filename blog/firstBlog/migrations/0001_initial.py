# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_title', models.CharField(max_length=20)),
                ('movie_text', models.TextField()),
                ('movie_date', models.DateTimeField(verbose_name=b'date published')),
                ('likes', models.IntegerField()),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]
