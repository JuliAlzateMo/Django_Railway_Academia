# Generated by Django 5.0.3 on 2024-03-18 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0018_alter_calificaciones_calificacion1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='calificacion1',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Nota 1'),
        ),
        migrations.AlterField(
            model_name='calificaciones',
            name='calificacion2',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Nota 2'),
        ),
        migrations.AlterField(
            model_name='calificaciones',
            name='calificacion3',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Nota 3'),
        ),
    ]
