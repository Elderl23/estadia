# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=80, choices=[(b'Sistemas', b'Sistemas'), (b'Redes', b'Redes'), (b'Mercadotecnia', b'Mercadotecnia')])),
            ],
            options={
                'ordering': ['tipo'],
                'verbose_name_plural': 'Categoria',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ciclos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('generacion', models.PositiveIntegerField()),
                ('mes_ini', models.CharField(max_length=80, choices=[(b'Enero', b'Enero'), (b'Febrero', b'Febrero'), (b'Marzo', b'Marzo'), (b'Abril', b'Abril'), (b'Mayo', b'Mayo'), (b'Junio', b'Junio'), (b'Julio', b'Julio'), (b'Agosto', b'Agosto'), (b'Septiempre', b'Septiembre'), (b'Octubre', b'Octubre'), (b'Noviembre', b'Noviembre'), (b'Diciembre', b'Diciembre')])),
                ('ano_ini', models.CharField(max_length=80)),
                ('mes_fin', models.CharField(max_length=80, choices=[(b'Enero', b'Enero'), (b'Febrero', b'Febrero'), (b'Marzo', b'Marzo'), (b'Abril', b'Abril'), (b'Mayo', b'Mayo'), (b'Junio', b'Junio'), (b'Julio', b'Julio'), (b'Agosto', b'Agosto'), (b'Septiempre', b'Septiembre'), (b'Octubre', b'Octubre'), (b'Noviembre', b'Noviembre'), (b'Diciembre', b'Diciembre')])),
                ('ano_fin', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['generacion'],
                'verbose_name_plural': 'Ciclos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=75)),
                ('tipo', models.CharField(max_length=25, choices=[(b'Asesor', b'Asesor'), (b'Alumno', b'Alumno')])),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Personas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=25)),
                ('asignatura', models.CharField(max_length=30, choices=[(b'Integradora I', b'Integradora I'), (b'Integradora II', b'Integradora II'), (b'Integradora III', b'Integradora III'), (b'Integradora IV', b'Integradora IV'), (b'Estadia TSU', b'Estadia TSU'), (b'Estadia ING', b'Estadia ING')])),
                ('estatus', models.BooleanField(default=True)),
                ('f_publicacion', models.DateField()),
                ('resumen', models.CharField(max_length=500)),
                ('asesor', models.ForeignKey(to='estadia.persona')),
                ('categoria', models.ForeignKey(to='estadia.categoria')),
                ('generacion', models.ForeignKey(to='estadia.ciclos')),
            ],
            options={
                'ordering': ['titulo'],
                'verbose_name_plural': 'Proyectos',
            },
            bases=(models.Model,),
        ),
    ]
