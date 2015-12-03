# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estadia', '0002_auto_20151021_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(max_length=80),
        ),
    ]
