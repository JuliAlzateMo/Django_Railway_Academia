# Generated by Django 5.0.3 on 2024-03-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0033_remove_estudiantes_rol_remove_profesores_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='ciudad',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='direccion',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='profesores',
            name='ciudad',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='profesores',
            name='direccion',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='fechaFin',
            field=models.DateField(default='2024-01-01', verbose_name='Fin'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='fechaInicio',
            field=models.DateField(default='2024-01-01', verbose_name='Inicio'),
        ),
    ]
