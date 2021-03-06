# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('seccion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(blank=True, max_length=50)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.Alumno')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.Materia')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='alumno',
            field=models.ManyToManyField(through='colegio.Nota', to='colegio.Alumno'),
        ),
        migrations.AddField(
            model_name='grado',
            name='materia',
            field=models.ManyToManyField(blank=True, to='colegio.Materia'),
        ),
    ]
