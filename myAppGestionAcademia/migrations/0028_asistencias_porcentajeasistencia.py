# Generated by Django 5.0.3 on 2024-03-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0027_calificaciones_fkprofesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencias',
            name='porcentajeAsistencia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]