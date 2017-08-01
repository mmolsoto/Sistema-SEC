# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-29 06:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenidos', '0003_curso_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pregunta', models.CharField(choices=[('Pregunta de desarrollo', 'Pregunta de desarrollo'), ('Seleccion m\xfaltiple', 'Seleccion m\xfaltiple'), ('T\xe9rminos pareados', 'T\xe9rminos pareados')], max_length=20)),
                ('pregunta', models.TextField()),
                ('dificultad', models.CharField(choices=[('B\xe1sica', 'B\xe1sica'), ('Intermedia', 'Intermedia'), ('Avanzada', 'Avanzada')], max_length=20)),
                ('imagen_pregunta', models.ImageField(blank=True, null=True, upload_to='Preguntas/')),
                ('observacion', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('count', models.IntegerField(blank=True, default=0, editable=False, null=True)),
                ('corregida', models.BooleanField(default=False)),
                ('rechazada', models.BooleanField(default=False)),
                ('cant_usada', models.IntegerField(blank=True, default=0, editable=False, null=True)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Asignatura')),
                ('contenido', models.ManyToManyField(blank=True, to='contenidos.Contenido')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Unidad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(blank=True, max_length=1, null=True)),
                ('respuesta', models.TextField()),
                ('imagen_respuesta', models.ImageField(blank=True, null=True, upload_to='Respuestas/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status_respuesta', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preguntas.Pregunta')),
            ],
        ),
    ]
