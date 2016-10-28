# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0003_auto_20161021_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
