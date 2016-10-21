# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCruzEstefania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name=b'Creado')),
                ('reporteDeAlguien', models.CharField(max_length=500)),
                ('numeroDeReporte', models.IntegerField()),
            ],
            options={
                'verbose_name': 'ModeloCruz',
            },
        ),
        migrations.CreateModel(
            name='UsuariosUaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usario', models.CharField(max_length=500)),
                ('expediente', models.IntegerField()),
                ('facultad', models.CharField(choices=[(b'Ciencias Naturales', b'Ciencias Naturales'), (b'Informatica', b'Informatica'), (b'Ingenieria', b'Ingenieria'), (b'Lenguas y Letras', b'Lenguas y Letras')], max_length=20)),
                ('promedio', models.FloatField()),
                ('dado_de_bajo', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='modelcruzestefania',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Front.UsuariosUaq'),
        ),
    ]
