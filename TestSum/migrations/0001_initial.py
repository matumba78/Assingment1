# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rollno', models.CharField(unique=True, max_length=10)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('Mobile_number', models.IntegerField(verbose_name='Mobile_number')),
                ('Address', models.CharField(max_length=20)),
                ('College', models.CharField(max_length=20)),
            ],
        ),
    ]
