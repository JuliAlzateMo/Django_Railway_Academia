# Generated by Django 5.0.3 on 2024-03-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0034_estudiantes_ciudad_estudiantes_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='ciudad',
            field=models.CharField(default='Medellin', max_length=100),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='ciudad',
            field=models.CharField(default='Medellin', max_length=100),
        ),
    ]
