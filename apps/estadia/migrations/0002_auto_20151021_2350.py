# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estadia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=25, choices=[(b'Asesor', b'Asesor'), (b'Alumno', b'Alumno')])),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Alumnos',
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='persona',
            new_name='asesor',
        ),
        migrations.AlterModelOptions(
            name='asesor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Asesores'},
        ),
        migrations.AddField(
            model_name='proyecto',
            name='alumno',
            field=models.ForeignKey(default=1, to='estadia.alumno'),
            preserve_default=False,
        ),
    ]
