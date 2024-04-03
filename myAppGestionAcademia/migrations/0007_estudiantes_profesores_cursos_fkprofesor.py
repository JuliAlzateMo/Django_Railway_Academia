# Generated by Django 5.0.3 on 2024-03-13 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0006_rename_fecha_cursos_fechacreacion_cursos_fechafin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('idEstudiante', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.ImageField(default=None, upload_to='estudiantes')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('idProfesor', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.ImageField(default=None, upload_to='profesores')),
                ('especialidad1', models.CharField(max_length=100)),
                ('especialidad2', models.CharField(blank=True, max_length=100, null=True)),
                ('especialidad3', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'db_table': 'Profesores',
            },
        ),
        migrations.AddField(
            model_name='cursos',
            name='fkProfesor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myAppGestionAcademia.profesores'),
        ),
    ]