# Generated by Django 5.0.3 on 2024-03-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0023_alter_asistencias_asistencia1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='fechaFin',
            field=models.DateField(default='2024-01-01', verbose_name='F.F.'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='fechaInicio',
            field=models.DateField(default='2024-01-01', verbose_name='F.I.'),
        ),
    ]
